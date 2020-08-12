


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "3e7ae27b-cf80-4f9b-bfde-4974c4bbe84c",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "a549d9bf-61ee-41a7-9795-913e745fe40d",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "edb3ebf7-e8c9-4ad6-b1da-87c0fb5f5180",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "436a3be8-dd6a-43e8-8961-ff4c1eb443be",
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

