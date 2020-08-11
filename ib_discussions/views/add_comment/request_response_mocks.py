

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "934ea299-4858-4937-bd4d-bc638a2e0dec"
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
        "user_id": "9fe2a342-2346-4803-8c37-c132313d7e15",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "f9e69202-ed22-439e-9f51-7d2d640815e2",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "b1a89c4d-8268-4a1e-af14-f531b092bd2c",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "c04fa0d4-8b03-4b7e-ada5-ece9a9666751",
            "format_type": "IMAGE",
            "url": "string",
            "thumbnail_url": "string"
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
    "res_status": "INVALID_USER_IDS"
}
"""

