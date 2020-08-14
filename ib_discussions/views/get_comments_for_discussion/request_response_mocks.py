


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "f61022de-005b-4058-8add-0439e4bdefd5",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "5928777d-7e24-414e-a7c1-b40ba811f0e2",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "aca19e2a-3833-4494-b8f3-7c9797f6bf6c",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "7e09aaa4-32e1-45bb-b9a7-9a11d5dbd5e6",
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

