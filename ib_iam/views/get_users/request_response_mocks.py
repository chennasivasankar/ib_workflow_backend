


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c9aaea63-c404-4807-aa56-70cd13857287",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ff9e2c2d-6693-43aa-b1e2-7b1c584e5707",
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
                "company_id": "6381cd1c-eb54-4877-945c-625f04215dee",
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

