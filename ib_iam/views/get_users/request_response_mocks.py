


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "e425a403-7c34-486e-ab84-419ea856d8c7",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "5b77b7eb-9ba3-4938-8b63-61fd2386d0f6",
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

