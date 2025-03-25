from fastapi import UploadFile, APIRouter
from services.validation_service import validation_service

validation_router = APIRouter()

@validation_router.post("/image")
async def postImage(json_file: UploadFile, png: UploadFile) -> object:
    try:
        return validation_service(json_file, png)
    except Exception as error:
        return error