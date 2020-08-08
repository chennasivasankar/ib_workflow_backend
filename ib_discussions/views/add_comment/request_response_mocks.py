

REQUEST_BODY_JSON = """
{
    "comment_content": "string"
}
"""


RESPONSE_200_JSON = """
{
    "author": {
        "user_id": "42a3a39d-235e-4641-82ba-6e04612dfee3",
        "name": "string",
        "profile_pic_url": "string"
    },
    "comment_id": "dae946d9-2324-41bb-b336-b649ce505ad1",
    "comment_content": "string",
    "total_replies_count": 1,
    "is_editable": true,
    "created_at": "2099-12-31 00:00:00"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "DISCUSSION_ID_NOT_FOUND"
}
"""

