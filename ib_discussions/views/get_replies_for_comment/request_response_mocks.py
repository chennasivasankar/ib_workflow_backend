


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "comment_id": "8e430fbb-b224-4490-82b8-b9869a7c039a",
            "author": {
                "user_id": "bb1faf26-f95b-4c75-967f-6e994b1c689a",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "7393cf99-ae2b-41b3-889f-d397cfa3f5fb",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "cfaf5e47-9905-491b-9892-bceae3d58c31",
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

