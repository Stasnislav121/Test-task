not_found_err_schema = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string"
                },
                "messages": {
                    "type": "object",
                    "additionalProperties": {
                        "type": "string"
                    }
                }
            },
            "required": ["message", "messages"]
        },
        "status": {
            "type": "string"
        }
    },
    "required": ["result", "status"]
}

internal_error_schema = {
    "type": "object",
    "properties": {
        "message": {
            "type": "string"
        },
        "code": {
            "type": "integer"
        }
    },
    "required": ["message", "code"]
}