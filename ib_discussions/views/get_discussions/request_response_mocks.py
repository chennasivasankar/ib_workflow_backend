

REQUEST_BODY_JSON = """
{
    "entity_id": "string",
    "entity_type": "TASK",
    "filter_by": "ALL",
    "sort_by": "LATEST"
}
"""


RESPONSE_200_JSON = """
{
    "discussions": [
        {
            "discussion_id": "afd25f2d-89e0-4c63-96bc-e25a9cbc7535",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "cdc0b2d4-4b6c-4cd5-bb32-66fb571c3ca8",
                "name": "string",
                "profile_pic_url": "string"
            },
            "is_clarified": true,
            "is_editable": true,
            "total_comments_count": 1
        }
    ],
    "total_count": 1
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET"
}
"""

