

REQUEST_BODY_JSON = """
{
    "members": [
        {
            "team_member_level_id": "76472240-be4e-4082-b05a-5b7499b5ebe3",
            "member_ids": [
                "46c5ce43-fc1e-4983-a6fe-ef0a45cc006f"
            ]
        }
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TEAM_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TEAM_MEMBER_LEVEL_IDS_NOT_FOUND"
}
"""

