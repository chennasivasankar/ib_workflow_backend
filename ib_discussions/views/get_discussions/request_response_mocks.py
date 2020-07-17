

REQUEST_BODY_JSON = """
{
    "entity_id": "string",
    "entity_type": "TASK"
}
"""


RESPONSE_200_JSON = """
{
    "discussions": [
        {
            "discussion_id": "string",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "string",
                "name": "string"
            }
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

