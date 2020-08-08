


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "448caa35-22ea-456d-8d93-f737c22ce0be",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "ba44a6f5-63af-459a-831d-1a326bacb02e",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "0277bbfd-f3bd-48a1-8849-882e1dd238bd",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "48df7f97-aa5d-4214-a527-fcca5c8b78be",
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

