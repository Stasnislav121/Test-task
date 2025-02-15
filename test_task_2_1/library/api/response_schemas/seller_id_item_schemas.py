seller_id_item_has_items_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "createdAt": {
                "type": "string",
                "format": "date-time"
            },
            "id": {
                "type": "string"
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
