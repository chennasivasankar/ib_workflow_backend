

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
            "discussion_id": "ca8e2244-925b-4c18-8725-cb757378845f",
            "description": "string",
            "title": "string",
            "created_at": "2099-12-31 00:00:00",
            "author": {
                "user_id": "94ab3a5d-04ff-4708-a1d2-1f34004d033a",
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

