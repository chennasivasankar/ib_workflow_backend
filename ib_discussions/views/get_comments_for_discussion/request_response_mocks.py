


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "1878e171-048d-4ac1-ad73-1a4567617310",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "a40a6e5a-b9aa-4082-8bd0-654f14724dd5",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "c784f3d0-5e33-40f4-8842-82b498b9a870",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "b1f93c85-7ffa-4928-878d-a217b7498665",
                    "format_type": "IMAGE",
                    "url": "string"
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

