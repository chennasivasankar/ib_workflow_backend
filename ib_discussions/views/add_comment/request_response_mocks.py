

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "f7d7aa5a-a976-469e-b68c-00a09348b81a"
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
        "user_id": "14472d4f-3e10-4e93-bc3e-d6f1e7a5750b",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "bcdcb35a-f8ef-4697-a098-0b3d8c3dcf20",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "7fc15ca9-8990-42ee-948f-e7efcadff371",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "6ecf25dd-d024-4e23-ae41-50a71221890f",
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

