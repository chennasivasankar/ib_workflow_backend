

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "comment_id": "8bebdfc0-255d-4405-a2ac-639f7eeaed8d",
    "author": {
        "user_id": "6aa0589d-0134-4df4-8cc9-42e404e2e82f",
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

