


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "5716e870-c49d-44d4-9412-6906e2d24f0c",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4b9c615b-870a-4a26-bed7-90d8d9b63d31",
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

