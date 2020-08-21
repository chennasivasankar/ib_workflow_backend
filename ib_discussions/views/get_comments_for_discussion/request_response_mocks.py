


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "8d7ae115-5a90-446c-a917-ca9697fcda7b",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "8b2641c4-47d8-4c28-b3da-54cb0a2f3a60",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "b336eff4-a137-4634-b857-7b662a64658f",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "0e5d2ddf-a387-4b62-a887-abda0c582c75",
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

