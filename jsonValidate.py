from jsonschema import validate, FormatChecker
from jsonschema.exceptions import ValidationError
from typing import Any, List, Dict
from schemas.alerts_schema import alerts
from schemas.status_update_schema import status_update

def isValidJson(jsonData: object, schemaData: Dict[str, Any]) -> bool:
  try:
    validate(instance=jsonData, schema=schemaData,format_checker=FormatChecker())
    return True
  except ValidationError:
    return False

def validateJsonToSchemas(jsonData: object, schemas: List[Dict[str, Any]]) -> bool:
  for schema in schemas:
    if isValidJson(jsonData, schema):
      return True
  return False

schemas = [alerts, status_update]

print(validateJsonToSchemas({"alert_id":1, "camera_id":1, "timestamp":"2025-03-24T07:12:42.218753Z", "status":"pending", "image_path":"asdas.png", "confidence":0.5,"user_id": "sas",}, schemas))