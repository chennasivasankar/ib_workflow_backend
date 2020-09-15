


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
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
                    "team_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
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

