

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "0280ed25-b6bc-4010-95d6-3c70ce0d9254"
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
        "user_id": "60af3d68-5ae7-4894-8f6b-50033ad96b7b",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "1098a61e-7c05-43fa-945e-7e54a71fb3c4",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "0ad16a52-18b3-454b-8ddb-09ffbe9d80cc",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "b1bacff9-8582-4b27-a780-33ad023180de",
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

