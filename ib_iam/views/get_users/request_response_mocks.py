


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "7d7d9904-7495-4596-b046-a46fd2342a15",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "e7518b4b-8129-453f-9994-c609ba6ec147",
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

