import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

export default function Register() {
    const navigate = useNavigate();
    const [form, setForm] = useState({
      username: "",
      email: "",
      password: "",
    });

    const handleChange = (e) => {
      setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
      e.preventDefault();
      try {
        await api.post("/auth/register", form);
        alert("Registered successfully");
        navigate("/login");
      } catch (err) {
        alert(err.response?.data?.detail || "Registration failed");
      }
    };

    return (
      <form onSubmit={handleSubmit}>
        <h2>Register</h2>
        <input name="username" placeholder="Username" onChange={handleChange} />
        <input name="email" placeholder="Email" onChange={handleChange} />
        <input
          name="password"
          type="password"
          placeholder="Password"
          onChange={handleChange}
        />
        <button type="submit">Register</button>
      </form>
    );
}
