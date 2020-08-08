


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "8b5d1220-28bc-4d27-bb5a-8138ee9baa7d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8490b6c0-3c77-4477-8575-8ded128e331d",
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

