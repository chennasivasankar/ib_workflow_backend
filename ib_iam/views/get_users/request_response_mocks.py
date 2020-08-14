


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d0432e8e-4deb-42cb-ba0e-e4de5c623170",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "048b6000-5a8d-4169-8bbe-2c0b95de805b",
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

