


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "e5cdd0ee-12b4-44da-975d-3cc827bb26ac",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "42c44be3-383f-4105-8acc-edeb47047b4a",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "8498139e-cd2a-46d3-8e35-91c3412022af",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "d56f0d8a-6654-49d9-8b0b-c78b9f093902",
                    "format_type": "IMAGE",
                    "url": "string",
                    "thumbnail_url": "string"
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

