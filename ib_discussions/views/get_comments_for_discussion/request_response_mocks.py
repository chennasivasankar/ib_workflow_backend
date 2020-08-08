


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "5c6e170d-f234-4117-8593-08db062c365f",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "98c1cdb7-c17e-46e6-8e55-b76b5d6f6752",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "c7fd8c6b-283b-4f20-9446-37813834de73",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "34014580-0d21-4421-bc38-193da049f508",
                    "format_type": "IMAGE",
                    "url": "string"
                }
            ]
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
    "res_status": "INVALID_OFFSET"
}
"""

