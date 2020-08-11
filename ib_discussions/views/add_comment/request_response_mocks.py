

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "91b6a870-0f91-438a-a457-288133824130"
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
        "user_id": "1a60550e-7b65-4bc9-b8f2-ab9908de9a5d",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "b1968072-8fec-477a-bf11-0b9f46909944",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "457b28dc-c653-4e44-a23e-0d35c83c290a",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "a4d89bf4-9422-498f-a941-9630f32ea398",
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

