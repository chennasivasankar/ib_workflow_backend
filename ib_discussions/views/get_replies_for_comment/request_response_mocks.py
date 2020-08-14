


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "ce364434-6d05-4a0f-919a-01fa5c605093",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "54e8622d-540e-475a-99fa-3c18a01a04d2",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "cb77af14-e871-41ae-9af9-2e8f9a14fd2e",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "1609bacd-d00b-4d90-941e-b19e53a2799c",
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

