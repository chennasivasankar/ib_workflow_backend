

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "4c45d5ab-aa0b-4dbf-97bd-5000bb45474d"
    ],
    "multimedia": [
        {
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "eec73571-1299-48c0-86db-21c0abb69e52",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "f97f14a6-5e86-4a66-b8d4-ab87e26466a2",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "5b04387e-a8e6-4211-a0f9-f729d17e4e5e",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "93d6351a-559c-4a7f-bbd7-522ea7c83661",
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
        }
    ],
    "total_replies_count": 1
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DISCUSSION_ID_NOT_FOUND"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USER_IDS"
}
"""

