


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "80e1ab54-6b16-466b-9578-693b4a4343a0",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "576db5e1-a024-4411-bd37-81d933fb0573",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "3db8808b-2c77-4fec-9b70-af789db46a26",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "ec4dc5e8-f378-4b6b-b8c1-6c9eca89819b",
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

