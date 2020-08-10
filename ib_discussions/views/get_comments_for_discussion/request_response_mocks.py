


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "16c07177-531a-4dec-bee9-3184c5436609",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "af10f8e3-e843-4857-8100-0f74e2dddeb1",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "3c41533e-c655-499c-99f6-5a879a62b175",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "4f855ccc-f822-4b10-bccf-f801f93a6fa0",
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

