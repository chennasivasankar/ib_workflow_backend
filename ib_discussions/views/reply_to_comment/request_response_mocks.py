

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "ce6dd72a-a030-4d03-a3ed-33a36f522c85"
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
    "comment_id": "3a0d9ca8-a162-4fc3-a054-2452ee0ff9dd",
    "author": {
        "user_id": "7cdcaa77-9b20-4c61-8e19-ec695f8afc71",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_content": "string",
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "b9408ef0-0712-495e-910e-4d2716cd4a34",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "69a45950-b451-46ed-9c45-13fde1fae0be",
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

