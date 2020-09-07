

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
            "discussion_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
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

