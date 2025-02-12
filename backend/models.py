from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Modèle Utilisateur
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Stocker le mot de passe hashé
    messages = relationship("Message", back_populates="user")

# Modèle des Messages
class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sport = Column(String)
    content = Column(String)

    user = relationship("User", back_populates="messages")
