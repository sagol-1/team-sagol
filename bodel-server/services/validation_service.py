from fastapi import HTTPException, UploadFile, status
import httpx
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas
import logging
from datetime import datetime

URL = "http://10.50.16.11:8000/data"

logging.basicConfig(
    filename='virus.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger("FastAPI-Virus")

async def validation_service(json: UploadFile, png: UploadFile) -> None:
    try:
        logger.info("Root endpoint accessed")
        is_type_correct = png.filename.lower().endswith('.png') and json.filename.lower().endswith('.json')
        is_files_valid = png_validation(png.file) and validateJsonToSchemas(json.file.read())
        if is_type_correct and is_files_valid:
            post_data(files_dict={'png': png.file, 'json': json.file})
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

async def post_data(files_dict: dict):
    httpx.post(URL, data=files_dict)