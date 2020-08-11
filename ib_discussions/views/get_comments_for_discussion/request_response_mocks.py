


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "868c3d43-6b77-41b6-80f4-b69a75c06adc",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "c05b6999-6cf9-4520-a90d-404152e01ba5",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "57898e1f-5b47-4497-82fb-c16a578110e9",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "f0025992-55d4-42a9-8fdf-45aec536187f",
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
    "res_status": "DISCUSSION_ID_NOT_FOUND"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET"
}
"""

