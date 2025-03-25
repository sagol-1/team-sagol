from fastapi import HTTPException, UploadFile
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas


def validation_service(json_file: UploadFile, png: UploadFile) -> None:
    is_valid = True

    try:
        if png.filename.lower().endswith('.png'):
            is_valid = is_valid and png_validation(png.file.read())
        else:
            is_valid = False
        if json_file.filename.lower().endswith('.json'):
            is_valid = is_valid and validateJsonToSchemas(json_file.file.read())
        else:
            is_valid = False

        return is_valid
    except:
        raise HTTPException(status_code=500)
    