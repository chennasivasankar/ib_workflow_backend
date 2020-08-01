


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "7a23b04e-47ed-4bfd-ac9b-10dfefc19119",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a757cfc7-f0d4-49ed-b001-f9edf067a427",
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
                "company_id": "c30892bf-65a6-4a33-b753-9ffc387079da",
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

