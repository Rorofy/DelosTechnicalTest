import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
    return (
        <div style={{ textAlign: "center", padding: "20px" }}>
            <h1>Bienvenue sur le Chatbot Sportif !</h1>
            <p>Choisissez un sport pour commencer à discuter avec notre chatbot :</p>
            <ul style={{ listStyleType: "none", padding: 0 }}>
                <li><Link to="/chat/football">Football</Link></li>
                <li><Link to="/chat/rugby">Rugby</Link></li>
                <li><Link to="/chat/tennis">Tennis</Link></li>
                <li><Link to="/chat/volley">Volley</Link></li>
                <li><Link to="/chat/cyclisme">Cyclisme</Link></li>
            </ul>
        </div>
    );
};

export default Home;
