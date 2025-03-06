from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    location = Column(String)
    status = Column(String, default="processing")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    tasks = relationship("Task", back_populates="project", cascade="all, delete")



class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String)
    status = Column(String, default="pending")
    project = relationship("Project", back_populates="tasks")
    
