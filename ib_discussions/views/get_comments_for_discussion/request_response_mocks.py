


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "50ef10c1-480a-49c1-a6ed-dfc355757854",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "acf8f860-ec63-41bd-8515-c5ab482b9b5a",
            "comment_content": "string",
            "replies_count": 1,
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

