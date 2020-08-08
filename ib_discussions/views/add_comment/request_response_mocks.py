

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "638fb92b-271e-4b2e-ab7b-6e1e904b2cf7"
    ],
    "multi_media": [
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
        "user_id": "7cdbeb3e-a895-4a22-9b9c-e78202a7ddab",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "c5f7bedb-7288-4c2f-bad4-4fefaa37d78e",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "33c43435-0cc8-4436-a23d-09520551085a",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multi_media": [
        {
            "multi_media_id": "c34613ad-c678-4730-b993-3a66b4ba4436",
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

