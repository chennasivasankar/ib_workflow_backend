

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "8874f2e9-efce-49b3-80da-9c2983a8f246"
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
        "user_id": "873d4764-5c52-4be0-b915-5bd04499b111",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "07fc4537-ada4-49fc-9643-0fb77394efc0",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "feecde6d-daad-4fca-9947-512baeaffb60",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "f40c87b6-d47c-4078-a6b3-26347e42fd23",
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

