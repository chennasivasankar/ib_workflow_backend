


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "85c2fcea-db51-4536-97db-e6d83b38fd13",
            "name": "string",
            "email": "string",
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "teams": [
                {
                    "team_id": "266bb031-c3b9-4040-8b68-3c33358c759d",
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

