


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "1b445a1e-23f2-4b7c-a513-b96bfef61b7b",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "b4d8b776-2038-4822-99cf-542ac90e406e",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "697d523d-9452-44e2-b0b3-2071e32302a9",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "a0b69716-42d9-495e-bfb9-e8bb36700710",
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

