


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c6337a0a-2cec-4f9c-b502-63b88f81db41",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4f36e8fb-d993-4566-b629-8a5c13156769",
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

