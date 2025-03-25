from fastapi import HTTPException, UploadFile
from filters.png_filter import png_validation
from filters.jsonValidate import validateJsonToSchemas


def validation_service(json: UploadFile, png: UploadFile) -> None:
    is_valid = True
    print("before png")

    try:
        if png.filename.lower().endswith('.png'):
            is_valid = is_valid and png_validation(png.file.read())
        else:
            is_valid = False
        
        print("png: " + is_valid)

        if json.filename.lower().endswith('.json'):
            is_valid = is_valid and validateJsonToSchemas(json.file.read())
        else:
            is_valid = False
        
        print("json: " + is_valid)

        return is_valid
    except:
        raise HTTPException(status_code=500)
    