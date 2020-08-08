


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "35de3839-4e92-4fd3-b97c-07c505dee312",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "6d47a9d4-c267-44dc-89d5-4ba8b8800fb1",
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

