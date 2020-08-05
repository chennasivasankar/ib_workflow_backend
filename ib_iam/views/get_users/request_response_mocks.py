


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "10cae777-f671-477d-b092-50bd20654c86",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6b1e4d94-316d-4e39-b48f-2cf7f5e378fb",
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

