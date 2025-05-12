# AI Task Manager Agent 🧐✅

An **Agentic AI System** that manages and organizes tasks given in natural language. Built using **FastAPI** and designed to simulate a lightweight AI-based task manager.


## 📌 Description

This AI Agent accepts task inputs in natural language, categorizes them, and stores them efficiently. It supports:

* 📥 Adding tasks
* 📒 Organizing tasks by category and status
* ✏️ Updating task details
* 🗑️ Deleting tasks
* 📃 Retrieving all tasks

This simulates a foundational AI-based task manager for productivity use cases.


## 🚀 Features

* FastAPI-powered RESTful API
* Task model with `title`, `description`, `status`, and `category`
* Supports CRUD operations
* JSON-based storage for simplicity
* Project structured in a scalable way


## 🧱 Tech Stack

* Python 3.11+
* FastAPI
* Pydantic
* Uvicorn


## 🐂 Folder Structure

```
AI_Task_Manager_Agent/
├── data/
│   └── tasks.json            # Stores tasks in JSON format
├── models/
│   └── .gitkeep              # Placeholder (optional model extensions)
├── utils/
│   └── .gitkeep              # Placeholder (helper functions in future)
├── src/
│   └── main.py               # Main FastAPI app
├── README.md
├── requirements.txt
```


## ⚙️ Installation & Run

1. **Clone the repo:**

   ```bash
   git clone https://github.com/D443-dk/AI_Task_Manager_Agent.git
   cd AI_Task_Manager_Agent
   
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Run the app:**

   ```bash
   cd src
   uvicorn main:app --reload
   

## 📬 API Endpoints

| Method | Endpoint      | Description    |
| ------ | ------------- | -------------- |
| GET    | `/tasks`      | Get all tasks  |
| POST   | `/tasks`      | Add a new task |
| PUT    | `/tasks/{id}` | Update a task  |
| DELETE | `/tasks/{id}` | Delete a task  |


## ✅ Final Notes

* Project tested via Postman for all CRUD operations.
* `models/`, `data/`, and `utils/` included for extensibility.
* Designed with clean code principles and API best practices.


## 📄 License

MIT License © 2025 Dinesh Kumar
