from fastapi import FastAPI
from .routes import router
from .celery_worker import complete_tasks
from celery.schedules import crontab
from .celery_worker import celery_app

app = FastAPI(title="AI Construction task manager")

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Construction Task Manager!"}


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(15.0, complete_tasks.s(), name="Complete tasks every 15 sec")