from typing import List
from fastapi import HTTPException, UploadFile
from filters.png_filter import png_validation
from filters.json_filter import json_validation

def validation_service(files: List[UploadFile]):
    try:
        for file in files:
            if file.filename.lower().endswith('.png'):
                png_validation(file)
            elif file.filename.lower().endswith('.json'):
                json_validation(file)
    except:
        raise HTTPException(status_code=500, detail="-> Something went wrong")
    