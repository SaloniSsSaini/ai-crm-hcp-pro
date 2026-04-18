from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String)
    summary = Column(Text)
    sentiment = Column(String)
    follow_up = Column(Text)