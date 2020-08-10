

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "1dbc72cb-53b2-4570-9251-e1dc41cfb38e"
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
        "user_id": "def6a013-014e-4f6f-817a-fecef960caa3",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "a81ccbdf-c543-4618-85d3-21637e38919f",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "607aa037-b68f-412e-a729-4873525e3b53",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "9f2a9a00-f876-48cf-af44-3f26329096c6",
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

