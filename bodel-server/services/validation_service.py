from fastapi import HTTPException, UploadFile
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas


def validation_service(json: UploadFile, png: UploadFile) -> None:
    print("before png")

    try:
        if png.filename.lower().endswith('.png') and json.filename.lower().endswith('.json'):
            return png_validation(png.file) and validateJsonToSchemas(json.file.read())
        else:
            return False
    except Exception as error:
        return HTTPException(status_code=500, detail="Something went wrong")
    