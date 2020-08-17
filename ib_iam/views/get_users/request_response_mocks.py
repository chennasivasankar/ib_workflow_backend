


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "f188809c-6234-47fb-8e8d-5cab07ddf819",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "63bed66e-6ddc-4eab-94e6-0c70e6cb7334",
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

