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
