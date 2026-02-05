import { useEffect, useState } from "react";
import api from "../services/api";

export default function Tasks() {
    const [tasks, setTasks] = useState([]);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [loading, setLoading] = useState(false);

    const fetchTasks = async () => {
    try {
        setLoading(true);
        const res = await api.get("/tasks/");
        setTasks(res.data);
    } catch (err) {
        console.error("Failed to load tasks", err);
    } finally {
        setLoading(false);
    }
};

const addTask = async (e) => {
    e.preventDefault();
    if (!title.trim()) return;

    try {
        await api.post("/tasks/", {
        title,
        description,
        });
        setTitle("");
        setDescription("");
        fetchTasks();
    } catch (err) {
        console.error("Failed to add task", err);
    }
};

const deleteTask = async (id) => {
    try {
        await api.delete(`/tasks/${id}`);
        setTasks((prev) => prev.filter((t) => t.id !== id));
    } catch (err) {
        console.error("Failed to delete task", err);
    }
};

const logout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
};

useEffect(() => {
    fetchTasks();
}, []);

return (
    <div className="page">
        <h2>My Tasks</h2>

        <div className="top-bar">
            <button className="secondary" onClick={logout}>
                Logout
            </button>
        </div>

        <form onSubmit={addTask}>
            <input
                placeholder="Task title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
            />

            <textarea
                placeholder="Task description"
                rows="3"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />

            <button type="submit">Add Task</button>
        </form>

        {loading ? (
            <p>Loading...</p>
        ) : (
                <div style={{ marginTop: "20px" }}>
                    {tasks.map((task) => (
                        <div key={task.id} className="task">
                            <div className="task-title">{task.title}</div>
                            {task.description && (
                                <div className="task-desc">{task.description}</div>
                            )}

                            <div className="task-actions">
                                <button className="secondary" onClick={() => deleteTask(task.id)}>  Delete </button>
                            </div>
                        </div>
                    ))}
                </div>
            )}
    </div>
);
}
