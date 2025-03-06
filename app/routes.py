from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Project, Task
from .schemas import ProjectSchema, ProjectCreateSchema
from .services import get_project_tasks


router = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/projects/", response_model=ProjectSchema)
async def create_project(request:ProjectCreateSchema, db:Session = Depends(get_db)):
    new_project = Project(project_name=request.project_name, location=request.location)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    tasks = await get_project_tasks(request.project_name)
    for task in tasks:
        db.add(Task(name=task["name"], status=task["status"], project_id=new_project.id))
    
    db.commit()
    return new_project

@router.get("/projects/{project_id}", response_model=ProjectSchema)
async def get_project(project_id:int, db:Session = Depends(get_db)):
    return db.query(Project).filter(Project.id == project_id).first()

