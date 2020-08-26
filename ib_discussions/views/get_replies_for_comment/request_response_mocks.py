


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "3c69d5f4-ccd8-4f61-8e23-cb93b57d83e5",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "3e74ceb5-6ebe-4735-aefe-6e7c9568fddf",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "4de93071-a2f4-47f5-93cb-3bb9ec5b2b20",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "58eb6cab-ce28-4e52-b5ed-ab2105578469",
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
    "res_status": "COMMENT_ID_NOT_FOUND"
}
"""

