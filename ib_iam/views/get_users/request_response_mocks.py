


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "64a8b575-8979-4b9f-b594-d87d53510852",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "13f1d97b-3502-498c-9a15-daa9bf459215",
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

