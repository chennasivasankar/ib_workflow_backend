


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c46f7044-00f6-4aed-8d47-96865eba8505",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "fea9667c-c7b4-4dda-a535-f0d2d7169aeb",
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

