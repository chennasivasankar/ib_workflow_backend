

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "9c9119e2-7efa-4bba-940a-866a97bb6619"
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
        "user_id": "5a938c66-f64d-45d0-afe9-0703081c4897",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "50deb63d-8a91-431b-8ade-7f9cff1c55db",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "6a61a49c-c37d-4d36-8d9b-3cc5283fec5d",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "a9b717ef-7515-4af7-8d7e-8be1b79a2616",
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

