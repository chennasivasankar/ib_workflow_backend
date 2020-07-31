


RESPONSE_200_JSON = """
{
    "total_teams_count": 1,
    "teams": [
        {
            "name": "string",
            "description": "string",
            "team_id": "string",
            "no_of_members": 1,
            "members": [
                {
                    "member_id": "string",
                    "name": "string",
                    "profile_pic_url": "string"
                }
            ]
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_LIMIT"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS"
}
"""

