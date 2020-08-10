


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "5a26efe0-4fa3-44b1-aa32-e2066ae92481",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "7ce78452-9fea-4fb1-8aea-d20269061f76",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "e7145ed3-cc97-49a5-9ce1-9baf3d3a0bbd",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "11fc2f10-487e-4a69-9a9f-96da7bae407d",
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

