


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9c1084f4-efeb-445a-b40f-7efe25065918",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "2a030692-456c-404e-9a75-273cbaaf23ce",
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

