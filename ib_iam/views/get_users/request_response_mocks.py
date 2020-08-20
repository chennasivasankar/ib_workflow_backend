


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "787f20f8-05a8-4a3f-af3b-15a6a2f3c715",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "1c1e58d0-08bd-4c11-992f-2819428d0202",
                    "team_name": "string"
                }
            ],
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "company": {
                "company_id": "string",
                "company_name": "string"
            }
        }
    ],
    "total": 1
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_LIMIT"
}
"""

