# AI-Powered Construction Task Manager

## Overview
This project is a FastAPI-based microservice that simulates an AI-powered construction task manager. It allows users to create construction projects, generate required tasks using the **Gemini Pro API**, store project data in an **SQLite database**, and retrieve project details. Additionally, it includes background task processing using **Celery and Redis** to simulate task completion over time.

---

## Features
- ✅ **FastAPI Endpoints** for project creation and retrieval
- ✅ **Gemini Pro API Integration** for generating construction tasks dynamically
- ✅ **SQLite Database** with SQLAlchemy for persistent storage
- ✅ **Celery and Redis** for background task processing (automatic task completion)
- ✅ **Celery Beat** for periodic execution of task updates (bonus feature)

---

## Setup Instructions
###  Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Redis (for Celery background tasks)

### Clone the Repository
```bash
 git clone <repo_url>
 cd construction_ai
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Initialize the Database
```bash
python -m app.database
```

### Start the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### Start Redis Server
```bash
redis-server
```

### Start Celery Worker
```bash
celery -A app.celery_worker worker --loglevel=info --pool=solo
```

### Start Celery Beat (For Periodic Task Completion)
```bash
celery -A app.celery_worker beat --loglevel=info
```

---

## API Usage Examples

### 1. Create a New Project
**Endpoint:** `POST /projects/`
```json
{
  "project_name": "Restaurant",
  "location": "San Francisco"
}
```
**Response:**
```json
{
  "id": 1,
  "project_name": "Restaurant",
  "location": "San Francisco",
  "status": "processing",
  "tasks": [
    {"name": "Find land", "status": "pending"},
    {"name": "Get permits", "status": "pending"},
    {"name": "Hire contractors", "status": "pending"}
  ]
}
```

### 2. Retrieve Project Details
**Endpoint:** `GET /projects/{project_id}`
```json
{
  "id": 1,
  "project_name": "Restaurant",
  "location": "San Francisco",
  "status": "in_progress",
  "tasks": [
    {"name": "Find land", "status": "completed"},
    {"name": "Get permits", "status": "pending"}
  ]
}
```

---

## 🚀 Conclusion
This AI-powered construction task manager efficiently handles project creation, task generation, and background task processing. It showcases the power of **FastAPI, Celery, Redis, and Gemini Pro API** in a real-world application. 🎯

