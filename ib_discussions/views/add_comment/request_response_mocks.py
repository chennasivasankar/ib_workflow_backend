

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "0ffc20a2-05a6-49c4-8eb5-c9f8bd2e6fe3"
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
        "user_id": "b66ee618-4ef3-43d7-9191-0d5a89769a19",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "98451ca4-3fe1-4ded-96a0-4bdc344be7ff",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "d605d90c-1173-4e12-92e1-09545d1775b1",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "1cad520a-cea8-4a02-8dc4-d8e9cf169b4c",
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

