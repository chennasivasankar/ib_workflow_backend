

REQUEST_BODY_JSON = """
{
    "comment_content": "string",
    "mention_user_ids": [
        "9bab612f-947d-4cdf-a855-28930311ee79"
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
        "user_id": "1574bf60-2480-4c33-8274-7bc4118857e4",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "1488fa2e-c209-4835-b61a-0bd0867db876",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00",
    "mention_users": [
        {
            "user_id": "a43c609c-a863-4129-88ce-2a4c5c1a1139",
            "name": "string",
            "profile_pic_url": "string"
        }
    ],
    "multimedia": [
        {
            "multimedia_id": "00ad9b60-c321-45be-84da-f3403b512e0c",
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

