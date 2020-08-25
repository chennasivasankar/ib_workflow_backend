


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "de66b915-0265-4f59-a7a6-54dbbc6a909f",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bba17696-5d91-4057-83eb-a9160d32caf9",
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

