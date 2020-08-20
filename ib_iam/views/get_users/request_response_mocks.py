


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "5f6ca2c5-4b21-429c-bd01-4ffa1a9d2de0",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "df87417e-68f0-4249-8339-1d7e53abd0ef",
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

