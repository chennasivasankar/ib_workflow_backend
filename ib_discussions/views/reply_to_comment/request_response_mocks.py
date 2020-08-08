

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "comment_id": "4c36e0f2-da82-41e3-88e3-5fc6cf53e801",
    "author": {
        "user_id": "f7fe6f6a-8624-4af9-8ec5-ed3c9dfa171a",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "COMMENT_ID_NOT_FOUND"
}
"""

