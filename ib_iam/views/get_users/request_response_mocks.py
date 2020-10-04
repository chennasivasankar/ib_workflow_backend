


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "a131901a-e7a1-439f-a9a0-63a5d6d6ef8e",
            "name": "string",
            "email": "string",
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "teams": [
                {
                    "team_id": "8170ed38-9247-472e-a32d-3edf2450d5d5",
                    "team_name": "string"
                }
            ],
            "is_email_verified": true,
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
    "res_status": "INVALID_LIMIT_VALUE"
}
"""

