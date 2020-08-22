


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "918c7354-532e-493d-80c1-8936511572ff",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "5a96baf7-a6b2-4093-8598-276a21b4d4c7",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "39ea5ead-0c21-4a9d-8a8a-d73ccbdb2d37",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "132354c1-e933-49e6-a39a-2f56738a3e0c",
                    "format_type": "IMAGE",
                    "url": "string",
                    "thumbnail_url": "string"
                }
            ],
            "total_replies_count": 1
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

