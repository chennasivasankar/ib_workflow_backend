


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9a488aa1-3a7f-4295-a100-6b8948a5c656",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "60a7c50c-3a21-41ca-8ef2-b2eccc0260a0",
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

