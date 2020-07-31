


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c5bb4a1e-8b2e-4417-b558-45954c5825cf",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "2a85c3e7-3c4b-4759-9f34-5afd4c8d5b52",
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
                "company_id": "63f62971-ee5d-47ff-be70-387f390787b0",
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

