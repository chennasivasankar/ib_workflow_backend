


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "0251ee05-1c8b-4aba-91bd-2a3f999c2e2b",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a0ad2ea0-1a43-4420-aa57-65fdc516765b",
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
                "company_id": "dbe20dfe-4bcc-4676-b11c-d3f1273b5f8f",
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

