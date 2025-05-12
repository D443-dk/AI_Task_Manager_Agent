from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

# Define the path to tasks.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)  # Ensure 'data' folder exists
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

# Task model
class Task(BaseModel):
    title: str
    description: str
    status: str  # "pending", "in_progress", "completed"
    category: str  # e.g., "Work", "Personal", etc.

# Utility: Load tasks
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Utility: Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to AI Task Manager Agent"}

# Get all tasks
@app.get("/tasks")
def get_tasks():
    return load_tasks()

# Add a new task
@app.post("/tasks")
def create_task(task: Task):
    tasks = load_tasks()
    tasks.append(task.dict())
    save_tasks(tasks)
    return {"message": "Task added successfully"}

# Update a task by index
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    tasks = load_tasks()
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[task_id] = task.dict()
    save_tasks(tasks)
    return {"message": "Task updated successfully"}

# Delete a task by index
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    tasks = load_tasks()
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.pop(task_id)
    save_tasks(tasks)
    return {"message": "Task deleted successfully"}
