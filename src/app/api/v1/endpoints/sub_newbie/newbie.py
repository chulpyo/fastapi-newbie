"""서브 뉴비"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def newbie_root():
    return {"message": "Hello World"}