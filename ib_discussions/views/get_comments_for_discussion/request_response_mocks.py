


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "b552f62b-aa21-4b54-90d0-cb5364156c37",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "3401438d-b353-4027-aa8e-22ac6882e1ce",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "71926975-ad5d-49c4-ba46-7529e3c08da9",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "cb968e43-bbf7-4472-9d5c-822402fb5381",
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

