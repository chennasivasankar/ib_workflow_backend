


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "17ef5f53-882a-4fc2-a7e5-3145b101c93a",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "dc7bcb81-7630-4c88-99f2-3ba10602ddc7",
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

