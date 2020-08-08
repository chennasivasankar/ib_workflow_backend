


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "88035b70-5b80-47b2-a11c-2a85b5f73eb3",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "1faaa6c8-5bba-4fc3-a71f-06b8e0b74fa2",
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

