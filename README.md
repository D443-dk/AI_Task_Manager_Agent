# AI-Based Task Manager Agent

## Project Overview

This project is a lightweight AI-based Task Manager Agent built using **FastAPI**. It allows users to manage tasks through a RESTful API: create, read, update, and delete tasks. Tasks are stored locally in a JSON file, which makes the setup simple without needing any external database.

---

## Problem Statement

Managing personal or team tasks manually can be inefficient. The goal was to automate this through a backend API system that supports:

* Creating tasks
* Updating tasks
* Deleting tasks
* Retrieving all tasks

---

## Solution Architecture

```
AI_Task_Manager_Agent/
│
├── src/
│   ├── main.py              # Main FastAPI app
│   ├── data/
│   │   └── tasks.json       # JSON storage for tasks
│   └── models/
│       └── task_model.py    # Pydantic model for task validation
│
└── packages/                # Pre-downloaded wheel files (optional)
```

* **FastAPI** for API backend
* **Uvicorn** as ASGI server
* **Pydantic** for data validation
* **tasks.json** as lightweight database


## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/yourusername/AI_Task_Manager_Agent.git
cd AI_Task_Manager_Agent
```

### 2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies (offline)

```
cd packages
pip install fastapi-*.whl
pip install starlette-*.whl
pip install uvicorn-*.whl
```

### 4. Start the FastAPI server

```
cd ..
cd src
uvicorn main:app --reload
```


## API Endpoints

### `GET /`

Returns a welcome message.

### `GET /tasks`

Returns the list of all tasks.

### `POST /tasks`

Creates a new task. Requires JSON body:

```json
{
  "title": "Complete assignment",
  "description": "Finish the AI Task Manager project"
}
```

### `PUT /tasks/{task_id}`

Updates a task with the given ID.

### `DELETE /tasks/{task_id}`

Deletes a task with the given ID.



## Walkthrough Video

Watch this full walkthrough  to understand the project, code, and usage:

🔗 [Watch on Vimeo]([(https://vimeo.com/1083479053?share=copy)]



## Highlights

* Fully functional CRUD API
* Local JSON storage (no DB setup required)
* Clean, modular codebase
* Offline installation supported


## Acknowledgements

Thanks to **OneData Software Solutions** for the opportunity to build this agentic AI system.
