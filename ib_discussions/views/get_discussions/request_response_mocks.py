

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
            "discussion_id": "1528870d-9677-4f71-b7b7-6eff8a5c9d7b",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "9db428f7-58c5-4c60-955b-29edec511368",
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

