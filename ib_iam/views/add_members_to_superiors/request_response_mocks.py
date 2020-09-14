

REQUEST_BODY_JSON = """
{
    "add_members_to_superior": [
        {
            "immediate_superior_user_id": "b0b4d5dc-e20d-40ac-b3d5-2bac342c4f0a",
            "member_ids": [
                "0a7f0365-91ad-4265-acad-f4dee3b29122"
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

