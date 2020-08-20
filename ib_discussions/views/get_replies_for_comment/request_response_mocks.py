


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "0ab02f66-ef4f-44bb-8876-438f76b6387c",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "37dd3032-ad13-4704-9d6e-8c7b50aa8f26",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "9bd1faf8-3aaa-42f1-90cb-5cb0fe41d7b4",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "b8cac528-1336-4ee8-9360-5a120273b42c",
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
    "res_status": "COMMENT_ID_NOT_FOUND"
}
"""

