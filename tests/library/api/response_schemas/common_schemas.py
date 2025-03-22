not_found_err_schema = {
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

bad_request_err_schema = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string"
                },
                "messages": {
                    "type": ["object", "null"],
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