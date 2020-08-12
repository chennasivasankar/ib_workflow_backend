

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "a1b378c5-3a92-4065-9b33-6379444c13db"
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
        "user_id": "db020821-9472-4579-8740-2558b1227e42",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "2807a5b8-403a-4fce-ba78-bce9053c0994",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "54511777-4d0c-49de-84a2-a1dfa7ac3336",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "6ccbbbb4-89dc-49f7-990a-93bc2a13344c",
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
        }
    ]
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "COMMENT_ID_NOT_FOUND"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USER_IDS"
}
"""

