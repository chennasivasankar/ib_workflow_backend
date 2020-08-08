

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "comment_id": "7cbb4174-26e7-4142-b9e0-6f25bb4388ca",
    "author": {
        "user_id": "15d0ce06-c4bd-4971-a460-08be6af2b2c7",
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

