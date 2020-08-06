

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
            "discussion_id": "5a145a41-9a9c-4af6-9e3f-34585a97e1d0",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "d14cf530-740f-47de-b71a-3e6d54c72389",
                "name": "string",
                "profile_pic_url": "string"
            },
            "is_clarified": true
        }
    ],
    "total_count": 1
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "ENTITY_ID_NOT_FOUND"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_ENTITY_TYPE_FOR_ENTITY_ID"
}
"""

