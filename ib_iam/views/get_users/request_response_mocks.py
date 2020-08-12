


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9e366faf-d67e-423c-9bff-ca4d27ecb779",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b9523524-690f-4a4d-82ae-398f0447c1ec",
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

