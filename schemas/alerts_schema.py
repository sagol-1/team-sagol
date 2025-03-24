alerts = {
      "type" : "object",
      "properties" : {
          "alert_id" : {"type" : "integer"},
          "camera_id": { "type": "integer" },
          "timestamp": { "type": "string", "format": "date-time" },
          "message": { "type": ["string", "null"] },
          "status": { "type": "string" },
          "image_path": { "type": "string" },
          "confidence": { "type": "number" },
          "user_id": { "type": ["string", "null"] }
      },
      "required": ["alert_id", "camera_id", "timestamp", "status", "image_path", "confidence"],
      "additionalProperties": False
}