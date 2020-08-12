


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "84d9b9fc-4cfa-4c81-bc64-02d773316026",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a629b600-43b8-4827-a570-63dec992a00f",
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

