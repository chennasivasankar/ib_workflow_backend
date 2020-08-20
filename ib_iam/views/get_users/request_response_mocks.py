


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "2abc2874-f1a1-4de0-8c8e-01e2bbde0dff",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "fbf9b2a1-dfab-421a-b40f-f7cb93e4aeeb",
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

