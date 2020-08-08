

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
        "user_id": "f87c74b6-461e-47ab-bff2-e4fc4931e505",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "b9533397-e445-4108-be18-70aac377d6b5",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "15b67290-ade6-4e80-a529-af4cf5560bf8",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "d197e52c-353c-474b-82b9-0a3cd78f753f",
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

