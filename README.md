
# AI Task Manager Agent

This is a simple **Agentic AI System** to manage your personal tasks using FastAPI (Python).  
It works 100% offline — no internet required after setup!


## Folder Structure

```
AI_Task_Manager_Agent/
├── src/
│   ├── main.py
│   └── tasks.json
├── packages/
│   ├── fastapi-*.whl
│   ├── uvicorn-*.whl
│   └── starlette-*.whl
└── venv/
```


##  How to Run the Project

###  1. Create and Activate Environment

```bash
cd AI_Task_Manager_Agent
python -m venv venv
venv\Scripts\activate
```

###  2. Install Packages Offline

```bash
cd packages
pip install fastapi-*.whl
pip install uvicorn-*.whl
pip install starlette-*.whl
```

###  3. Start the API Server

```bash
cd ..\src
uvicorn main:app --reload
```

##  API Documentation

After running the server, open in browser:

```
http://127.0.0.1:8000/docs
```

This will open Swagger UI — you can **test all API endpoints here**.


##  Available APIs

| Method | Endpoint         | Description        |
|--------|------------------|--------------------|
| GET    | /tasks           | Get all tasks      |
| POST   | /tasks           | Add a new task     |
| PUT    | /tasks/{task_id} | Update a task      |
| DELETE | /tasks/{task_id} | Delete a task      |

###  Sample JSON for POST

```json
{
  "title": "Finish Project",
  "description": "Complete the AI Agent Task before deadline",
  "status": "Pending"
}
```


##  JSON Data File

All tasks are stored in:

```
src/tasks.json
```

You can also open and edit this manually.


## Final Output Sample

When server is running:
- Visiting `http://127.0.0.1:8000/` shows:
  ```json
  {
    "message": "Welcome to AI Task Manager Agent"
  }
  ```

- Full testing can be done via Swagger UI or Postman.



## Author

Made by [Dinesh Kumar] for the OneData AI/ML Engineer Assignment 
