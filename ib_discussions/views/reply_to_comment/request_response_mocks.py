

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "0b1dee3c-9896-4b96-81b0-61c50aee2607"
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
    "comment_id": "78aff7fd-e8a8-4949-bdc4-9d0bdf4d142c",
    "author": {
        "user_id": "3bc734bb-f1f8-4e22-844f-3eb746831e02",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "79fc4ef8-51a5-49d7-8d9a-16cc73e94802",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "625fdf6d-1373-4010-aea6-3911cf7c61eb",
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
    "res_status": "COMMENT_ID_NOT_FOUND"
}
"""

