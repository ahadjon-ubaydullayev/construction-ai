# from celery import Celery
# from sqlalchemy.orm import sessionmaker
# from .database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .models import Task

# # Initialize Celery
# celery_app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

# @celery_app.task
# def complete_tasks():
#     db: Session = SessionLocal()

#     try:
#         tasks = db.query(Task).filter(Task.status == "pending").all()
#         if tasks:
#             for task in tasks:
#                 task.status = "completed"
#             db.commit()
#             print(f"✅ Completed {len(tasks)} tasks.")
#     finally:
#         db.close()



from celery import Celery
from celery.schedules import crontab
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Task

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def complete_tasks():
    db: Session = SessionLocal()
    try:
        tasks = db.query(Task).filter(Task.status == "pending").all()
        if tasks:
            for task in tasks:
                task.status = "completed"
            db.commit()
    finally:
        db.close()


celery_app.conf.beat_schedule = {
    "complete-tasks-every-15-sec": {
        "task": "app.celery_worker.complete_tasks",
        "schedule": 15.0, 
    }
}

celery_app.conf.timezone = "UTC"
