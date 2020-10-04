

REQUEST_BODY_JSON = """
{
    "add_members_to_superior": [
        {
            "immediate_superior_user_id": "8c2431fc-3cd2-4f1b-9965-cd183b8d9242",
            "member_ids": [
                "1d71618d-b222-4f42-9b70-232db01b6d2d"
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
    "res_status": "TEAM_MEMBER_IDS_NOT_FOUND"
}
"""

