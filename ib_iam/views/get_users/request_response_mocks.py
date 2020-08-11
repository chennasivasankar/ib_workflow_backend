


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "601e4da4-d822-4074-a4cf-eace87ee8c52",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bd1704d7-5029-422a-be01-c5ef0f5f93b5",
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

