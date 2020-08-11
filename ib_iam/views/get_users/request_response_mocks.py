


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "0b77941c-403a-460c-be5e-c6d0388d733e",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "9a86bc8d-e5d6-4c72-a305-4e7731f356ba",
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

