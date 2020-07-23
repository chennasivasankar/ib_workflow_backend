


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "string",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4bf591e5-85fe-40b2-9ef4-35d84dac346c",
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
                "company_id": "7e8bb1c8-3977-4760-a6fb-018bd7c49fb4",
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

