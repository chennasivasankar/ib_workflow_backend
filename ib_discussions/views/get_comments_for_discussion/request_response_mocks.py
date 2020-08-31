


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "b19c0699-5841-4298-af2d-d42e7f882da4",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "e5b6f0c7-ff79-4a73-8668-04b08b307c3f",
            "comment_content": "string",
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "0489872e-8b4e-4683-885b-26030b92090b",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "7c3cbdd2-d2e8-4b78-80d1-84a84e2ec24b",
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

