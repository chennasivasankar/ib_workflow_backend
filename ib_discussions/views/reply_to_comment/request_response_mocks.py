

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "dd82c6c4-3d2b-4e27-a2a2-e5cc2c9f284c"
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
        "user_id": "b69decf2-0ac3-4ac6-b247-84451e035e84",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "9cd933db-3624-43a5-a04e-8e7cb0ac1228",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "be2e4210-8f3b-4b3b-9cb4-d8ad6cea573b",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "c8bbec66-08c5-4110-b877-51446497f455",
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

