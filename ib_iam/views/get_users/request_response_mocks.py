


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "335bf920-0a58-43e2-9e77-e867c53ff246",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a1394d13-f595-4672-9568-386f7f4251e7",
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

