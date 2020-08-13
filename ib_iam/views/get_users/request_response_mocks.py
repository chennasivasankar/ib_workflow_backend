


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d4b3cd84-a891-447a-8c50-6dc30bf611c8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8109722f-44dd-46db-b141-4a692889a7ec",
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

