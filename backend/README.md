# Task Manager Backend

A simple **task management REST API** built with **FastAPI**, allowing users to register, login, and manage tasks with full CRUD functionality.

---

## Features
- User authentication using **JWT**
- Create, read, update, and delete tasks
- **PostgreSQL** database integration
- Structured logging and error handling
- Test coverage using **Pytest**

---

## Tech Stack
- **Backend:** FastAPI, Python
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Authentication:** JWT
- **Testing:** Pytest

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/SanikaTodkar/Task_Manager.git
cd task-manager
```
### 2. Create a virtual environment
```bash
pipenv install
pipenv shell
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure environment variables
Create a `.env` file in the root directory and add the following:

### 5. Database Setup
Make sure you have PostgreSQL installed and running. Create a database for the application:

createdb task_manager_db
``` bash
DATABASE_URL=postgresql://username:password@localhost/task_manager_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### 6. Run the server
```bash
uvicorn app.main:app --reload
```

### 7. API Documentation
Once the server is running, you can access the interactive API documentation at:
```http://localhost:8000/docs
```
## Example API Requests
### Register a new user
```bash
POST/api/v1/auth/register
{
    "username": "testuser",
    "email": "testuser@example.com",
    "password": "password123"
}
```
### Login
```bash
POST/api/v1/auth/login
{
    "username": "testuser",
    "password": "password123"
}
```
### Create a new task
```bash
POST/api/v1/tasks/
Authorization: Bearer <access_token>
{
    "title": "New Task",
    "description": "Task description"
}
```
### Get all tasks
```bash
GET/api/v1/tasks/
Authorization: Bearer <access_token>
```
### Update a task
```bash
PUT/api/v1/tasks/{task_id}
Authorization: Bearer <access_token>
{
    "title": "Updated Task Title",
    "description": "Updated description"
}
```
### Delete a task
```bash
DELETE/api/v1/tasks/{task_id}
Authorization: Bearer <access_token>
```
## Running Tests
To run the test suite, use the following command:
```bash
pytest
```
## License
This project is licensed under the MIT License.