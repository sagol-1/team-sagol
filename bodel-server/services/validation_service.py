from fastapi import HTTPException, UploadFile, status
import httpx
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas

URL = "http://10.50.16.11:8000/data"


async def validation_service(json: UploadFile, png: UploadFile) -> None:
    if png.filename.lower().endswith('.png') and json.filename.lower().endswith('.json'):
        if png_validation(png.file) and validateJsonToSchemas(json.file.read()):
            post_data(files_dict={'png': png.file, 'json': json.file})
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def post_data(files_dict: dict):
    httpx.post(URL, data=files_dict)