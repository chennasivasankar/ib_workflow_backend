


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4411c8d2-b2b8-4f5c-92c0-87c52876494c",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "e288e4b4-b5b8-44bd-a16e-a82efebe9876",
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

