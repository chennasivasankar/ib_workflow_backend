


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "60c602b2-5d67-4bc8-8368-5c679aef9564",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "c7f78461-4c4c-4c64-b514-7280cb2ea958",
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
                "company_id": "bda6c4e0-0e51-4a5e-95b5-4099a05e6147",
                "company_name": "string"
            }
        }
    ],
    "total": 1
}
"""

RESPONSE_403_JSON = """
{
    "response": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

