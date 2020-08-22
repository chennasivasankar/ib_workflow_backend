


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "aff1c739-148c-4d68-8cac-fc3e164b580d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ce0a1fed-547b-4aa4-9296-d52375c49e6e",
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

