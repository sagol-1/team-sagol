from jsonschema import validate, FormatChecker
from jsonschema.exceptions import ValidationError
from typing import Any, List, Dict
from schemas.alerts_schema import alerts
from schemas.status_update_schema import status_update
from json import loads
from schemas.alerts_schema import alerts
from schemas.status_update_schema import status_update

def isValidJson(jsonData: object, schemaData: Dict[str, Any]) -> bool:
  try:
    # What validate expect instance to be?
    validate(instance=jsonData, schema=schemaData,format_checker=FormatChecker())
    return True
  except ValidationError:
    return False

def validateJsonToSchemas(jsonData: object, schemas: List[Dict[str, Any]] = [alerts, status_update]) -> bool:  
  instance_json = loads(jsonData)
  for schema in schemas:
    if isValidJson(instance_json, schema):
      return True
  return False


