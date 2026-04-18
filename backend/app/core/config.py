import os

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "YOUR_API_KEY")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/ai_crm"
    )

settings = Settings()