


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "935a544b-57b3-4e97-9cde-f9264c44df2a",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "98760263-0b53-4990-99a3-1e0ffea1c59a",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "f1a4d85f-1fd7-40cc-8b7e-8e1db8e05b7f",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "5cb487b8-011c-43a1-98fb-595ae041023a",
                    "format_type": "IMAGE",
                    "url": "string",
                    "thumbnail_url": "string"
                }
            ],
            "total_replies_count": 1
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

