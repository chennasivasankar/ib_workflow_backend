


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "4016a4b2-fbed-4a5e-9937-008965576a5b",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "deeb11b7-538a-4115-ab27-996e31b18780",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "1e870afb-e533-4199-abe8-a5d26ff557f0",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "c562cfd1-5541-4d02-a40b-199f1a1f022d",
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

