


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4116c6f3-ec4b-4d83-a58b-12d6f923d078",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a3fcf911-4d1f-4bd7-8852-a6b8175f47c7",
                    "team_name": "string"
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

