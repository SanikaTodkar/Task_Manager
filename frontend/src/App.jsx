import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Tasks from "./pages/Tasks";
import "./styles/app.css"

const isAuthenticated = () => !!localStorage.getItem("token");

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />

      <Route
        path="/tasks"
        element={
          isAuthenticated() ? <Tasks /> : <Navigate to="/login" />
        }
      />
    </Routes>
  );
}

export default App;
