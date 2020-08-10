


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "comment_id": "78876f48-d8c8-4894-b609-48ca0b548c5a",
            "author": {
                "user_id": "6b049cf5-29dd-49d4-b2ca-e4b54503d589",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "c8465c85-8a1e-4094-8292-b99c5aef5204",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "4d3f63bc-9f46-454d-b5ee-88a646e6a190",
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

