


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "8e3ed2fa-75a0-4eb5-9bea-fafbd9d180cd",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "9acfe85e-62fa-40c1-87c0-7e5425d1872d",
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

