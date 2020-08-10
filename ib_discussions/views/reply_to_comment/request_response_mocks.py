

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "30ce1a14-0674-48fb-9c5e-6e69d116ff71"
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
    "comment_id": "b48adb1d-07ba-48f5-a3a9-38a19739317d",
    "author": {
        "user_id": "79d72a7b-a2d0-4972-a291-3ab9891c41be",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "89a954f9-0d19-458a-a089-16bf77dd325e",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "f588331a-36a6-442a-9b57-13e53fd9b9e1",
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

