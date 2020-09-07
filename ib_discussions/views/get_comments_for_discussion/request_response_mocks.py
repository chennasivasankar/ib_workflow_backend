


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
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

