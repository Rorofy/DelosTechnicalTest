import React, { useEffect, useState } from "react";
import axios from "axios";

const Admin = () => {
    const [stats, setStats] = useState<{ user: string; questions: number }[]>([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/admin/stats")
            .then(response => setStats(response.data))
            .catch(error => console.error("Erreur de chargement des stats", error));
    }, []);

    return (
        <div>
            <h2>Admin - Statistiques des utilisateurs</h2>
            <table>
                <thead>
                    <tr>
                        <th>Utilisateur</th>
                        <th>Questions posées</th>
                    </tr>
                </thead>
                <tbody>
                    {stats.map((stat, index) => (
                        <tr key={index}>
                            <td>{stat.user}</td>
                            <td>{stat.questions}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Admin;