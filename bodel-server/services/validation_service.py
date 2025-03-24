from typing import List
from fastapi import HTTPException, UploadFile
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas


def validation_service(files: List[UploadFile]) -> None: 
    try:
        isValid = True
        for file in files:
            if file.filename.lower().endswith('.png'):
                isValid = isValid and png_validation(file.file.read())
            elif file.filename.lower().endswith('.json'):
                isValid = isValid and validateJsonToSchemas(file.file.read())
        return isValid
    except:
        raise HTTPException(status_code=500, detail=" -> Something went wrong")
    