

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "dd47eb61-b44a-4936-aea4-67cedd395b48",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "451e6f29-5d82-4452-b74b-d57e7287848a",
    "comment_content": "string",
    "replies_count": 1,
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

