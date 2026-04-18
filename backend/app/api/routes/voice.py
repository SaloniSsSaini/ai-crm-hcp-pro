from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/")
async def voice(file: UploadFile = File(...)):
    return {"text": "demo transcript"}