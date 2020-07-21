


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b4612e04-3fbc-4ca2-9941-334253f2abf8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "d2d0a3f0-9fe1-4a71-b31b-b0ed4a82c148",
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
                "company_id": "beaeaf44-39e6-4899-98cc-10427d59b42a",
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

