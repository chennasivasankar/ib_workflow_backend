


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "3f132e3e-e17a-49a4-b0a7-a2baa97e3a8d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6f483865-2c35-495f-b916-fa856e9982d8",
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

