


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "comment_id": "0e67d770-7c62-46de-a3ec-35333e9acd77",
            "author": {
                "user_id": "8c6cd769-776d-4293-83fc-f7cdcb4a6085",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "54524b60-207a-426c-82ce-9a1a1231d9c6",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "66874472-92bb-42ed-9623-2d4b6dab212d",
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

