get_item_statistic_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "contacts": {
                "type": "integer"
            },
            "likes": {
                "type": "integer"
            },
            "viewCount": {
                "type": "integer"
            }
        },
        "required": ["contacts", "likes", "viewCount"],
        "additionalProperties": False
    }
}

get_item_statistic_not_found_err_schema = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string"
                },
                "messages": {
                    "type": ["null", "array"]
                }
            },
            "required": ["message"]
        },
        "status": {
            "type": "string"
        }
    },
    "required": ["result", "status"]
}