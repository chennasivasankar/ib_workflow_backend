

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "b1d5acdc-c0de-478d-91f8-e89d9bc922ac",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "f51759cc-325a-4faa-9548-8b0c66090d0b",
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

