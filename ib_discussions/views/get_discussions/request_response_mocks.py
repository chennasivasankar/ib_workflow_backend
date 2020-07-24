

REQUEST_BODY_JSON = """
{
    "entity_id": "95c20a42-597b-4228-81dd-41e080d8848e",
    "entity_type": "TASK",
    "filter_by": "ALL",
    "sort_by": "LATEST"
}
"""


RESPONSE_200_JSON = """
{
    "discussions": [
        {
            "discussion_id": "fe7e6014-0d67-4759-b8f1-a620c14c3325",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "f57f4fed-fc67-46e1-a9d6-fb90599da821",
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

