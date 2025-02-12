import React, { useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import './Chat.css';

const Chat = () => {
    const { sport } = useParams();
    const [messages, setMessages] = useState<string[]>([]);
    const [input, setInput] = useState("");

    const sendMessage = async () => {
        const response = await axios.get(`http://127.0.0.1:8000/chat/${sport}`);
        setMessages([...messages, response.data]);
    };

    return (
        <div>
            <h2>Chatbot - {sport?.toUpperCase()}</h2>
            <div>
                {messages.map((msg, index) => (
                    <p key={index}>{msg}</p>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
            />
            <button onClick={sendMessage}>Envoyer</button>
        </div>
    );
};

export default Chat;
