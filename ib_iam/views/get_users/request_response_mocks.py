


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "fee41ebc-11cf-4fb6-84dd-edbf8b9dd358",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "f0b2b984-f372-4ad7-9b7f-75f6448b9c2e",
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
                "company_id": "c77e55b7-95a6-4fde-9be6-3bf9604463a3",
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

