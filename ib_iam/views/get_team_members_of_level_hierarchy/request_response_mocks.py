


RESPONSE_200_JSON = """
{
    "members": [
        {
            "member_id": "string",
            "name": "string",
            "profile_pic_url": "string",
            "immediate_superior_team_user_id": "string"
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

