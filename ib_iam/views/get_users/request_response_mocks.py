


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "cda02bbe-c115-4be9-aaae-84af12022b66",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "0d98a395-fa5a-4e42-ae34-099b33a3edfc",
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
                "company_id": "c84249c7-5d39-4430-bcec-2422f375399b",
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

