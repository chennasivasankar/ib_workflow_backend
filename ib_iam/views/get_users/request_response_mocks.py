


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "087495ed-c1b3-45ee-b548-551610ebe8db",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "fbe699b0-465d-4c0b-8b4c-6da6def1bacc",
                    "team_name": "string"
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

