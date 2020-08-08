

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "37b59d15-9c2b-4cf5-8a5b-356e742cb9e8"
    ],
    "multimedia": [
        {
            "format_type": "IMAGE",
            "url": "string"
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "comment_id": "8558be51-dfc0-4bc4-aac4-fdb844bc7304",
    "author": {
        "user_id": "6e7600a2-b641-42d8-a059-e0433395d420",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "e0323d2e-fbf1-469b-8417-ddee91c09c06",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "8ea35d7f-3a4e-4d1a-8f80-4c0f98b9286a",
            "format_type": "IMAGE",
            "url": "string"
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

