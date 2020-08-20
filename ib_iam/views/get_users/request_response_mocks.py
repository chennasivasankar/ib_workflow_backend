


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "17871384-2a9a-4093-8226-ca9428214e67",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "aff74a2d-a347-44d9-a03e-0cd6d858bab7",
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

