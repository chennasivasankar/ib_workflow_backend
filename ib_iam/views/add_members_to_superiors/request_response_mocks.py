

REQUEST_BODY_JSON = """
{
    "add_members_to_superior": [
        {
            "immediate_superior_user_id": "61058b14-16a9-4728-b925-0afad49ad0ef",
            "member_ids": [
                "b8103cae-3986-4692-8df4-e3f53ac4808f"
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

