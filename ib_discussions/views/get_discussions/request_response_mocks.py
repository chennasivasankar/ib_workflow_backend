

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
            "discussion_id": "b8fc9b75-ffcf-4654-8c0d-8fd69933c4d4",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "8357b089-1430-4871-8a87-b284da51bff8",
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

