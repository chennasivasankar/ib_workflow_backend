

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "d11abfdd-a92e-469a-844b-75ba321988b8",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "7da013bf-92a4-4af9-ada0-96ae4bc82215",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DISCUSSION_ID_NOT_FOUND"
}
"""

