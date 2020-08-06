


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "6e41a6b0-d8ae-4324-959e-ec4786974624",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "aafb9eaf-8653-434d-9421-ee060166da85",
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

