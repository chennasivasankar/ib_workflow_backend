


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d9332e53-ec56-47a4-93c7-2654c24d2e42",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ab2c2850-7254-470e-a925-c9ae44a19d4e",
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

