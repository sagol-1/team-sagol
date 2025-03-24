status_update = {
  "type": "object",
  "properties": {
    "alert_id": { "type": "integer" },
    "message": { "type": ["string", "null"] },
    "status": { "type": "string" },
    "user_id": { "type": ["string", "null"] },
  },
  "required": ["alert_id", "status"],
  "additionalProperties": False
}