from typing import List
from fastapi import UploadFile, APIRouter
from services.validation_service import validation_service

validation_router = APIRouter()

@validation_router.post("/multi")
async def check(files: List[UploadFile]) -> object:
    try:
        return validation_service(files)
    except Exception as error:
        return error
    
    return {"state": 200}