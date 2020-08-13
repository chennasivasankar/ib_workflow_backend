


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "6e0162fe-a344-4c89-8c19-f8a47a59e497",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b40ada51-4eba-4d0e-b4ac-adc71c07179a",
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

