


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "string",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a2b07e2e-46e4-428e-b8ae-ad34a0e68a41",
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
                "company_id": "a42ba754-522f-42d3-ba81-b9587c297b18",
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

