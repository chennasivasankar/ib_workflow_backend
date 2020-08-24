


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "47ac1443-856d-4d55-8629-24bd457d73c8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bf771cb4-80af-4d09-846e-39085a9fd1ed",
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

