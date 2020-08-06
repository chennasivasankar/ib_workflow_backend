


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b575489a-c3f6-4d1c-bfdf-8c16faabca57",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "e1c61b10-09ac-4d20-9657-14e2afa280f6",
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

