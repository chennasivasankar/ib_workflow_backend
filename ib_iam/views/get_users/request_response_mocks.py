


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "1580cd73-567d-4cb6-a840-715aea36cb41",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ebe50485-0fb0-4601-b8b6-b8218f3f95ae",
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
                "company_id": "8d818227-291c-47b8-86c0-09471a5a1d0a",
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

