


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "0ed54a13-57c3-4639-badf-700f5c4784dc",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "9d4ad61e-2bf7-4adf-9322-4744412fe34e",
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
                "company_id": "1a9ad4c9-2dcb-46d5-88d3-23e2522dee1e",
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

