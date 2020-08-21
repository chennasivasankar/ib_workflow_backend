


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "1f460ef6-49c6-4198-b520-7d46e7bfbd3c",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "feedacc3-3bee-4327-8029-1545de7f1d46",
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

