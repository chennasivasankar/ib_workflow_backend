


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "dfc34545-78b9-4bb8-a723-22839efc3ff2",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "67a962e3-f30f-4b05-9564-5319b4c57010",
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
                "company_id": "86db2e8e-e62c-4e6d-a6d1-89a53cc667dd",
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

