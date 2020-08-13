


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "729722b4-256f-44b6-ab7f-35f561ed2782",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "fb52930e-d4de-43e6-879a-e53ce4fdb9fb",
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

