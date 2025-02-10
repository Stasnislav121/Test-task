add_item_schema = {
    "type": "object",
    "properties": {
        "status": {
            "type": "string"
        }
    },
    "required": ["status"]
}

get_item_data_by_id_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "createdAt": {
                "type": "string",
                "format": "date-time"
            },
            "id": {
                "type": "string",
                "format": "uuid"
            },
            "name": {
                "type": "string"
            },
            "price": {
                "type": "number"
            },
            "sellerId": {
                "type": "integer"
            },
            "statistics": {
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
                "required": ["contacts", "likes", "viewCount"]
            }
        },
        "required": ["createdAt", "id", "name", "price", "sellerId", "statistics"]
    }
}

get_item_err_schema = {
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


get_item_not_found_err_schema = {
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

