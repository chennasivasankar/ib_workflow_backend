


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b920874e-8984-4a26-b3fc-e5a24a3b2fcb",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "342e5f41-d135-4954-96f2-2a09b488295b",
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

