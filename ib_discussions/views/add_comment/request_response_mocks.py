

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "37cea4c1-ad24-4e7f-95b3-35aab25a4c4e",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "c4221f4c-a016-49da-87b8-8118a6c6295f",
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

