


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "cfb2f6d7-9283-471f-905b-e0248bc8a585",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "7b3df32a-8b7c-42b6-ba79-399afe6f3b99",
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

