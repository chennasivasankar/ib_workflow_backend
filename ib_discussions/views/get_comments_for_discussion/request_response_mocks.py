


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "7155cabe-d982-4c2b-861f-7a216eea5bab",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "beb8cf8a-ef24-45cf-9a21-f0647f15cc23",
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

