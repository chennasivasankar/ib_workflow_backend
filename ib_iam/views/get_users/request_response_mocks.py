


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "38904c98-9aa9-4e54-9799-43263994e509",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6b23d447-307e-445e-bbe6-d7dc2b6c9e97",
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

