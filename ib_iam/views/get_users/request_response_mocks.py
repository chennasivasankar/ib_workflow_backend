


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "dc2d07bd-f90e-4d1f-8350-b72d62245bd8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "155179c5-e490-4e1b-8c14-cf643a152c7b",
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

