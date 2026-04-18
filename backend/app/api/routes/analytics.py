from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.interaction import Interaction

router = APIRouter()

@router.get("/")
def analytics(db: Session = Depends(get_db)):
    total = db.query(Interaction).count()
    positive = db.query(Interaction).filter(
        Interaction.sentiment == "positive"
    ).count()

    return {"total": total, "positive": positive}