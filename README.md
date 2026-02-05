✅ Task Manager – Full Stack Application

    A full-stack Task Manager application built using FastAPI (Backend) and React (Frontend).
    This project allows users to register, log in, and manage personal tasks securely using JWT authentication.
    
---
    
🎯 Built as an internship-ready project focusing on APIs, reliability, and clean architecture.

✨ Key Features

    🔐 User authentication (Register & Login)

    🛡️ JWT-based secure APIs

    📝 Create, view, and delete tasks

    👤 User-specific task isolation

    ⚙️ REST API with proper validation & error handling

    🧪 Basic backend tests

    🎨 Simple, clean frontend UI

---

🧰 Tech Stack
    🖥️ Frontend
    
        - React (Vite)
        - JavaScript
        - HTML & CSS

    Axios (API integration)

    ⚙️ Backend

        - FastAPI
        - Python
        - SQLAlchemy
        - PostgreSQL
        - JWT Authentication
        - Pydantic schemas

---

📁 Project Structure

    Task_Manager/
    │
    ├── README.md              # Project overview
    │
    ├── backend/               # FastAPI backend
    │   ├── README.md
    │   ├── app/
    │   ├── tests/
    │   └── Pipfile
    │
    └── frontend/              # React frontend
        ├── README.md
        ├── src/
        └── package.json

---

🚀 Getting Started
    ▶️ Backend Setup
        cd backend
        pip install pipenv
        pipenv install
        pipenv shell
        uvicorn app.main:app --reload


    📍 Backend runs at
    
        http://127.0.0.1:8000


    📘 Swagger Docs
    
        http://127.0.0.1:8000/docs

    ▶️ Frontend Setup
        cd frontend
        npm install
        npm run dev


    🌐 Frontend runs at
    
        http://localhost:5173

 ---

🔑 Authentication Flow

    1️⃣ User registers with username, email, and password
    2️⃣ User logs in and receives a JWT access token
    3️⃣ Token is stored in browser local storage
    4️⃣ Token is sent with API requests via headers
    5️⃣ Each user can only access their own tasks

---

🧪 Testing

    Basic backend tests are included for:
    
    Authentication
    
    Task APIs
    
    Run tests using:
    
        pytest

---

🎯 Why This Project?

    This project was built to:
    
        - Practice backend API development
        
        - Understand authentication & authorization
        
        - Work with databases and ORM
        
        - Integrate frontend with REST APIs
        
        - Follow real-world project structure
        
        - Build an interview-ready full-stack project

---

👩‍💻 Author

    Sanika Todkar
    
    GitHub: 👉 https://github.com/SanikaTodkar
