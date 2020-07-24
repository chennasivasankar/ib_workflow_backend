


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b63b44ae-1524-4cd9-8685-113161b7b7aa",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "1fb925d5-6b96-41f4-be0f-94a52fdb004a",
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
                "company_id": "5ca4b62a-56aa-4080-9d09-e34d0a964040",
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

