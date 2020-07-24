

REQUEST_BODY_JSON = """
{
    "entity_id": "0d7aafcf-bdf0-4c39-a9fb-409604c82462",
    "entity_type": "TASK",
    "filter_by": "ALL",
    "sort_by": "LATEST"
}
"""


RESPONSE_200_JSON = """
{
    "discussions": [
        {
            "discussion_id": "19c99baf-aadd-411e-96e3-07949cfbd5a7",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "9e30e3a5-3ed8-419f-acce-5fd76863004a",
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

