


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "125c95dc-a8c3-43a3-80b1-cfad5f4e7b46",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "291934c0-91d9-4154-8bff-5a6f031343b2",
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

