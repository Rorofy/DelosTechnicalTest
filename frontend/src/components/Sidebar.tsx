// Sidebar.tsx
import React from "react";
import { Link } from "react-router-dom";
import './Sidebar.css';

const Sidebar = () => {
    return (
        <div className="sidebar">
            <ul>
                <li><Link to="/">Accueil</Link></li>
                <li><Link to="/chat/football">Football</Link></li>
                <li><Link to="/chat/rugby">Rugby</Link></li>
                <li><Link to="/chat/tennis">Tennis</Link></li>
                <li><Link to="/chat/volley">Volley</Link></li>
                <li><Link to="/chat/cyclisme">Cyclisme</Link></li>
            </ul>
        </div>
    );
};

export default Sidebar;
