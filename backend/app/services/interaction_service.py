from sqlalchemy.orm import Session
from app.models.interaction import Interaction
from typing import Dict, Any


def create_interaction(db: Session, data: Dict[str, Any]):
    interaction = Interaction(
        hcp_name=data.get("hcp_name"),
        summary=data.get("summary"),
        sentiment=data.get("sentiment"),
        follow_up=data.get("follow_up"),
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_all_interactions(db: Session):
    return db.query(Interaction).all()


def get_interactions_by_hcp(db: Session, hcp_name: str):
    return db.query(Interaction).filter(
        Interaction.hcp_name == hcp_name
    ).all()


def update_interaction(db: Session, interaction_id: int, data: Dict[str, Any]):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if not interaction:
        return None

    interaction.summary = data.get("summary", interaction.summary)
    interaction.sentiment = data.get("sentiment", interaction.sentiment)
    interaction.follow_up = data.get("follow_up", interaction.follow_up)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(db: Session, interaction_id: int):
    interaction = db.query(Interaction).filter(
        Interaction.id == interaction_id
    ).first()

    if interaction:
        db.delete(interaction)
        db.commit()

    return {"status": "deleted"}