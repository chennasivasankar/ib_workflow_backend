

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "comment_id": "555b3691-d7cc-41de-9737-3d04ead0b1d4",
    "author": {
        "user_id": "4e25a839-59e7-4f05-814c-73183c75f094",
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

