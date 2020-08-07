


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "8bfc9a3b-69c4-4286-b9cc-4ae81055d450",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "22be894f-8e46-4a92-b27d-369d54615d2c",
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

