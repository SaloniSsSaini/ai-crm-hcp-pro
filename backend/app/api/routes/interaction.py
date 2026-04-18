from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.interaction import Interaction
from app.schemas.interaction_schema import InteractionCreate

router = APIRouter()

@router.post("/")
def create(data: InteractionCreate, db: Session = Depends(get_db)):
    obj = Interaction(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return db.query(Interaction).all()