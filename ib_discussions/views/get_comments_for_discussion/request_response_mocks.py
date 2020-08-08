


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "ed2fbb44-88ec-43a8-b18d-66792a9b74ea",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "67d03d3f-deeb-4dbc-8cfe-57746eadbff6",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "92a2f8eb-e6c0-4647-8d23-00ca74d2c95f",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "6672d245-b49b-4c53-833b-ed867c95e53c",
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

