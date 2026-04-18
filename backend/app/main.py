from fastapi import FastAPI
from app.api.routes import chat, interaction, analytics, voice
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chat.router, prefix="/chat")
app.include_router(interaction.router, prefix="/interaction")
app.include_router(analytics.router, prefix="/analytics")
app.include_router(voice.router, prefix="/voice")