from fastapi import HTTPException, Response, UploadFile, status
import httpx
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas

URL = "http://10.50.16.11:8000/data"


def validation_service(json: UploadFile, png: UploadFile) -> None:
    print("before png")

    try:
        is_type_correct = png.filename.lower().endswith('.png') and json.filename.lower().endswith('.json')
        is_files_valid = png_validation(png.file) and validateJsonToSchemas(json.file.read())
        if is_type_correct and is_files_valid:
            post_data(files_dict={'png': png.file, 'json': json.file})
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        return "ok"
    except Exception:
        return HTTPException(status_code=500)

async def post_data(files_dict: dict):
    httpx.post(URL, data=files_dict)