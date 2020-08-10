

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "37b59d15-9c2b-4cf5-8a5b-356e742cb9e8"
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
    "comment_id": "dcca155b-923e-40c7-a48e-467ad85a42b4",
    "author": {
        "user_id": "42d5543d-13b7-4736-902e-a4b150c7b598",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "e0323d2e-fbf1-469b-8417-ddee91c09c06",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "8ea35d7f-3a4e-4d1a-8f80-4c0f98b9286a",
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

