from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database import engine, Base, SessionLocal, get_db
from models import User, Message
import random
import asyncio
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuration de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Autoriser les requêtes provenant de cette origine
    allow_credentials=True,
    allow_methods=["*"],  # Permet toutes les méthodes HTTP
    allow_headers=["*"],  # Permet tous les headers
)

# Création des tables dans la base de données
Base.metadata.create_all(bind=engine)

# Gestion du hashage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Sports disponibles
SPORTS = ["football", "rugby", "tennis", "volley", "cyclisme"]

# Simule des réponses aléatoires par sport
def generate_sport_response(sport: str):
    return f"{sport.upper()} " * random.randint(10, 20)

# --- AUTHENTIFICATION ---

@app.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()
    return {"message": "Utilisateur créé avec succès !"}

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Identifiants incorrects")
    return {"message": "Connexion réussie", "user_id": user.id}

# --- CHATBOT AVEC STREAMING ---

@app.get("/chat/{sport}")
async def chat(sport: str):
    if sport.lower() not in SPORTS:
        raise HTTPException(status_code=400, detail="Sport non pris en charge")

    async def generate_response():
        response = generate_sport_response(sport)
        for word in response.split():
            yield word + " "
            await asyncio.sleep(0.1)

    return StreamingResponse(generate_response(), media_type="text/plain")

# --- HISTORIQUE DES CONVERSATIONS ---

@app.get("/history/{user_id}")
async def get_history(user_id: int, db: Session = Depends(get_db)):
    messages = db.query(Message).filter(Message.user_id == user_id).all()
    return messages

@app.post("/save_message")
def save_message(user_id: int, sport: str, content: str, db: Session = Depends(get_db)):
    message = Message(user_id=user_id, sport=sport, content=content)
    db.add(message)
    db.commit()
    return {"message": "Message enregistré"}

# --- STATISTIQUES ADMIN ---

@app.get("/admin/stats")
def get_stats(db: Session = Depends(get_db)):
    stats = db.query(User).all()
    return [{"user": user.username, "questions": len(user.messages)} for user in stats]

# --- WEBSOCKET POUR LE CHAT EN TEMPS RÉEL ---
@app.websocket("/ws/{sport}")
async def websocket_endpoint(websocket: WebSocket, sport: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            response = generate_sport_response(sport)
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client déconnecté")
