from pydantic import BaseModel

class InteractionCreate(BaseModel):
    hcp_name: str
    summary: str
    sentiment: str
    follow_up: str

class InteractionOut(InteractionCreate):
    id: int

    class Config:
        from_attributes = True