


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "015e16d2-1a26-45d0-adbf-2829ae0f6e71",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "86100e5a-137f-4345-bfb0-cfdfabe02741",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "5227bd3a-88e9-4073-a81b-c2958ad694bd",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "4b149b7e-6b68-4f47-9eac-14c5e1184d7c",
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

