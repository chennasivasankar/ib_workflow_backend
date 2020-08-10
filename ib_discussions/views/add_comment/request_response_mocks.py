

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "187fe395-d38d-463a-b5b9-a11b3eeb828f"
    ],
    "multimedia": [
        {
            "format_type": "IMAGE",
            "url": "string"
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "7cdce5c7-31a2-4e6d-92dd-70eee559b3fa",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "eef59a85-b9f3-40fc-8025-f21b86749652",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "50d56121-4ad4-40a2-a4eb-fc937e984cec",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "c8c1d8a9-c3d1-439a-8038-eccfdb129c15",
            "format_type": "IMAGE",
            "url": "string"
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

