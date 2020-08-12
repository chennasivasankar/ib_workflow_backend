


RESPONSE_200_JSON = """
{
    "comments": [
        {
            "author": {
                "user_id": "de879593-948f-46ac-8742-e9eb66af5f92",
                "name": "string",
                "profile_pic_url": "string"
            },
            "comment_id": "ff18aa3b-9e53-4a70-97e0-fa94c45ae741",
            "comment_content": "string",
            "total_replies_count": 1,
            "is_editable": true,
            "created_at": "2099-12-31 00:00:00",
            "mention_users": [
                {
                    "user_id": "ce22fc9c-dcbd-45c8-93ef-7fdff287ff9e",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ],
            "multimedia": [
                {
                    "multimedia_id": "d5418549-fdb9-4f47-a944-f0b54dafb1c1",
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

