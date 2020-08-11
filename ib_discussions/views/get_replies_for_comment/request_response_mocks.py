


RESPONSE_200_JSON = """
{
    "replies": [
        {
            "comment_id": "45abcb8f-725e-4226-af73-ab8002fefc07",
            "author": {
                "user_id": "4c9530d9-079a-418d-b771-869e17ddc50a",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "a7431a90-3c01-44f0-847d-d443467eb5de",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "0a87637a-1466-42a0-b187-9dc40822a639",
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

