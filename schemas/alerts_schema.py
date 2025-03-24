alerts = {
      "type" : "object",
      "properties" : {
          "alert_id" : {"type" : "integer"},
          "camera_id": { "type": "integer", "minimum": 1, "maximum": 20 },
          "timestamp": { "type": "string", "format": "date-time" },
          "message": { "type": ["string", "null"] },
          "status": { "type": "string", "enum": ["pending", "condemned", "cleared"] },
          "image_path": { "type": "string", "pattern": "^.*\\.png$" },
          "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
          "user_id": { "type": ["string", "null"] }
      },
      "required": ["alert_id", "camera_id", "timestamp", "status", "image_path", "confidence"],
      "additionalProperties": False
}