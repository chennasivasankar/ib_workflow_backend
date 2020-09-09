

REQUEST_BODY_JSON = """
{
    "add_members_to_superior": [
        {
            "immediate_superior_user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
            "member_ids": [
                "89d96f4b-c19d-4e69-8eae-e818f3123b09"
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

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TEAM_MEMBER_IDS_NOT_FOUND"
}
"""

