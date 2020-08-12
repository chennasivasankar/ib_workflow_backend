


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "36afc700-f94d-4526-a212-610ffe5739d4",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ab7c7d55-110c-45b4-b88e-3ec11e905559",
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

