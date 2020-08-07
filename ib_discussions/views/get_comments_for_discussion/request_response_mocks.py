


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "927c6669-dfb6-4a44-80ac-77ae05ab7d22",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "d7d534db-9f96-46d2-a4a0-b98f83ef639a",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00"
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

