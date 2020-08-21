


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "d9f9dad1-dcd9-4736-9cd3-02d74287666f",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "c9bf1010-a092-4324-9ccd-5517b6f14b06",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "d9bc1eb2-ec10-49a1-9713-e39802bca6a3",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "ecf576d2-485b-405e-a2f0-010351f261d4",
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

