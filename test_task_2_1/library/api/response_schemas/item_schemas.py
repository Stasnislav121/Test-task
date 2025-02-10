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