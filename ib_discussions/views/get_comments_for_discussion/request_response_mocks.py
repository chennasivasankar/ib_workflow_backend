


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "60dd7b33-85e4-4f13-8955-a3d564f5ee64",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "b3cb5e08-d6ed-4bee-bbee-03b628ac8ed5",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "8b284d80-ba01-4770-b0bd-e2399ed8796f",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "0c7352e3-f269-46ea-a9d7-8c0c75e1b043",
                    "format_type": "IMAGE",
                    "url": "string",
                    "thumbnail_url": "string"
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

