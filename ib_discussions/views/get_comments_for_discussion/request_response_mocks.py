


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "5d491ad9-d5d0-437d-8b11-cef59a541420",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "4c5c98b1-6427-43a7-8cd3-bfdbd7c89daf",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "5fd40c1a-424a-435c-8c8d-8eae4d0a5c39",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "a77da739-cc40-4da6-94dc-da9fe4a9faf1",
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

