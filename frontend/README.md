📝 Task Manager – Frontend

This is the frontend of the Task Manager application built using React + Vite.
It allows users to register, log in, and manage their tasks (create, view, and delete tasks) by communicating with a FastAPI backend.

🚀 Tech Stack

React (Hooks)

Vite

Axios – API communication

React Router DOM – Routing

CSS – Simple, clean styling

📂 Features

User Registration

User Login (JWT Authentication)

Create Tasks (Title + Description)

View Tasks

Delete Tasks

Logout

Protected Routes

📁 Project Structure
frontend/
├── src/
│   ├── pages/
│   │   ├── Login.jsx
│   │   ├── Register.jsx
│   │   └── Tasks.jsx
│   ├── services/
│   │   └── api.js
│   ├── styles/
│   │   └── app.css
│   ├── App.jsx
│   └── main.jsx
├── index.html
├── package.json
└── README.md

⚙️ Setup Instructions
1️⃣ Install dependencies
npm install

2️⃣ Start development server
npm run dev


The app will run at:

http://localhost:5173

🔗 Backend Dependency

Make sure the FastAPI backend is running before using the frontend.

Backend base URL (used in Axios):

http://localhost:8000/api/v1

🔐 Authentication Flow

JWT token is stored in localStorage

Token is automatically attached to API requests using Axios

Protected routes redirect unauthenticated users to /login