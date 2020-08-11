


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "a652f8e5-897b-4809-adc3-239013446d96",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4f92ebed-596d-4972-92fb-8e87271e336f",
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

