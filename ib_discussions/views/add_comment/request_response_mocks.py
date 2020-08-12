

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "fbff220a-29d3-412c-b1cc-9fb6221a7057"
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
        "user_id": "850d40b0-1c3e-4293-8e1b-66e48fc05d84",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "f9d00496-22e0-4402-9901-68fdb0cdf917",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "caa75ed1-8768-4d50-9ecd-e553c3255934",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "ad8f26b6-5840-474b-8a9f-b7cb60859a6b",
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

