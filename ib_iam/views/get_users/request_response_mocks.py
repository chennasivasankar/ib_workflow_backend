


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "6d05a09e-4ac6-4cba-ba1c-77ef8cdeabda",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6e5381a1-698f-4499-be29-3a980e60e77b",
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

