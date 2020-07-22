


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "string",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "64e9b7a7-eaff-4738-b1f6-df8888ae0e4b",
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
                "company_id": "96a62d10-3b7c-49a7-bc82-697dee1e0508",
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

