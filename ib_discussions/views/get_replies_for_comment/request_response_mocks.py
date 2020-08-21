


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "author": {
                "user_id": "7242d2ee-3fa6-4dcf-9d89-338d3f765066",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "892f5fa7-4c79-4914-98f4-d69c4b01ae3e",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "cc42c45b-a401-42af-8db3-dd355386be53",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "7422f55d-64b2-47fb-b67b-0725a324eb11",
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

