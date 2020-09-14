

REQUEST_BODY_JSON = """
{
    "members": [
        {
            "team_member_level_id": "94a0c9e4-95d8-4e0b-83d0-f2737cfe14eb",
            "member_ids": [
                "8dbee5cc-4b94-4f1c-9341-f0fb8d7dc53b"
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

