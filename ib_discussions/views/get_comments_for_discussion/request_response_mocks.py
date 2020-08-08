


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "87328381-6987-4d86-b6a2-dd00c4d3db4b",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "a2c97cb3-2dbc-49fd-b452-50d94ca8919d",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "70b22c7d-66ca-443d-98f7-6c193e482527",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multi_media": [
                {
                    "multi_media_id": "f0bb8b13-0fa1-4035-b595-6e150eee861f",
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

