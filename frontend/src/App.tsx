import React from "react";
import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Chat from "./components/Chat";
import Login from "./pages/Login";
import Admin from "./pages/Admin";
import './App.css'; // Importer le fichier CSS global

const App = () => {
    return (
        <>
            <Sidebar />
            <div className="main-content">
                <Routes>
                    <Route path="/" element={<div>Bienvenue sur l'application !</div>} />
                    <Route path="/chat/:sport" element={<Chat />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/admin" element={<Admin />} />
                </Routes>
            </div>
        </>
    );
};

export default App;
