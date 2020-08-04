


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "5706e06e-f830-49a8-a32a-f1ef25e9c48d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "d4e04f5d-4d20-4d2a-aecd-2f40837fd58f",
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
                "company_id": "f4da2119-48b7-4f30-82c8-72d3f0dc2e71",
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

