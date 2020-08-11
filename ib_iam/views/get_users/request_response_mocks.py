


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "f82d3cd1-1d33-40d7-ae70-bff941c5a9e4",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ba23eba0-f395-4d60-bb37-5ab8dbd2980a",
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

