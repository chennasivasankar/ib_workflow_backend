


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c2fc112e-9eff-42e8-bbc7-2b09a9639375",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "1e003f2c-fb98-4618-897b-250efc236e7f",
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
                "company_id": "9a3ccd1e-338b-44b9-b416-51fbda79d456",
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

