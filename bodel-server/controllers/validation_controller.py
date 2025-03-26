from fastapi import UploadFile, APIRouter, HTTPException, status
from services.validation_service import validation_service

validation_router = APIRouter()

@validation_router.post("/image")
async def postImage(json: UploadFile, png: UploadFile) -> object:
    try:
        return validation_service(json, png)
    except Exception as error:
        return error