


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "ef6dd6dd-5b51-46c4-964e-586f3db15d54",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "c4650e01-14a5-4814-a3ab-0a879c5cba1d",
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

