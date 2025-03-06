from pydantic import BaseModel
from typing import List, Optional


class TaskSchema(BaseModel):
    name:str
    status:str

    class Config:
        from_attibutes = True


class ProjectCreateSchema(BaseModel):
    project_name:str
    location:str

    class Config:
        from_attributes = True


class ProjectSchema(BaseModel):
    id:int
    project_name:str
    location:str
    status:str
    tasks:List[TaskSchema] = []

    class Config:
        from_attributes = True
        
