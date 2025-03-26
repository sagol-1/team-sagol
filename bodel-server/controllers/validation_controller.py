from fastapi import UploadFile, APIRouter, Response, HTTPException, status
from services.validation_service import validation_service

validation_router = APIRouter()

@validation_router.post("/image")
async def postImage(json: UploadFile, png: UploadFile) -> object:
    try:
        await validation_service(json, png)

        return Response(status_code=status.HTTP_200_OK)
    except Exception as error:
        if isinstance(error, HTTPException):
            return Response(status_code=error.status_code)
        else:
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)