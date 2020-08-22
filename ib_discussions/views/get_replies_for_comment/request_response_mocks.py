


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "da61a168-6be8-45a3-a7f0-a47097991fba",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "c24df9cf-7f56-4567-a9e8-f11bbe8ab690",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "8e216034-6ca6-43c9-a5e3-8f71d81a8ee8",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "5a65ff71-217a-4d05-adcc-b34b9f639bf3",
                    "format_type": "IMAGE",
                    "url": "string",
                    "thumbnail_url": "string"
                }
            ]
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

