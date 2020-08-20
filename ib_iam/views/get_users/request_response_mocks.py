


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "0fc6102a-19cb-4579-ac2b-df67c9845275",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "60786ed9-e734-4323-aad0-d13aee8ce785",
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

