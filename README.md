🗂️ Task Manager Application

A full-stack Task Manager application that allows users to register, log in, and manage their personal tasks securely.
The project is built using FastAPI for the backend and React for the frontend, following clean architecture and REST API principles.

🚀 Features

User registration and login

JWT-based authentication

Create, view, and delete tasks

Tasks are user-specific (private)

Clean separation of frontend and backend

RESTful API design

Simple and intuitive UI

🛠️ Tech Stack
Frontend

React (Vite)

JavaScript

HTML & CSS

Axios for API calls

Backend

FastAPI

Python

SQLAlchemy

SQLite (can be extended to PostgreSQL/MySQL)

JWT Authentication

Pydantic schemas

📂 Project Structure
Task_Manager/
├── README.md          # Project overview
├── backend/           # FastAPI backend
│   ├── README.md
│   ├── app/
│   ├── tests/
│   └── Pipfile
└── frontend/          # React frontend
    ├── README.md
    ├── src/
    └── package.json

⚙️ How to Run the Project
1️⃣ Backend Setup
cd backend
pip install pipenv
pipenv install
pipenv shell
uvicorn app.main:app --reload


Backend will run at:

http://127.0.0.1:8000


API Docs:

http://127.0.0.1:8000/docs

2️⃣ Frontend Setup
cd frontend
npm install
npm run dev


Frontend will run at:

http://localhost:5173

🔐 Authentication Flow

User registers with username, email, and password

User logs in and receives a JWT token

Token is stored in local storage

Authenticated requests include the token in headers

Users can only access their own tasks

🧪 Testing

Backend includes basic tests for:

Authentication

Task APIs

Run tests using:

pytest

🎯 Purpose of This Project

This project was built to:

Understand full-stack development

Practice REST API design

Learn authentication and authorization

Gain hands-on experience with FastAPI and React

Build a real-world, interview-ready project

👩‍💻 Author

Sanika Todkar

GitHub: SanikaTodkar

📌 Future Improvements

Update and complete task functionality

Better UI styling

Task status (completed / pending)

Pagination and search

Deployment using Docker / Cloud
