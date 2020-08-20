


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "d8f46e7a-dac4-4085-9b46-28e284f25271",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "0059f172-8c7b-4e0e-b078-f23e2671de32",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "30a9be87-0f05-4b86-8c92-d5505bc9fd8d",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "5d00ee6f-5857-4ba7-9eb5-927fa3d4de3a",
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

