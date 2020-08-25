


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "156a14dc-05ec-483a-82a2-656268a48890",
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
                    "team_id": "3edc0e6a-1251-447c-b867-1172fc48faa8",
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

