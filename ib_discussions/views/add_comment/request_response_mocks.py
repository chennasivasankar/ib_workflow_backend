

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "66ae7d03-1fcc-4315-8949-d7c83b4b45ca"
    ],
    "multimedia": [
        {
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
        }
    ]
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "86c6ec02-7461-40c9-956e-3a21bf03555c",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "56d9149f-764a-4777-b26c-2fe4427a2d4d",
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "9160df93-52e9-4f89-9b82-128fb614e72c",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "aef2e976-19be-415a-b5f6-569b2922826c",
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
        }
    ],
    "total_replies_count": 1
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
    "res_status": "INVALID_USER_IDS"
}
"""

