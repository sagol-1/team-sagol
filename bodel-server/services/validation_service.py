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
                send_data(png, json)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Files invalid.")
        return "Files sent."
    except Exception as error:
        return HTTPException(status_code=500, detail="Something went wrong -> " + error)

def send_data(png: UploadFile, json: UploadFile):
    httpx.post(URL, data={'png': png, 'json': json})