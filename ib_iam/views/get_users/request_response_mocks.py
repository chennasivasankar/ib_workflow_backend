


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "string",
            "name": "string",
            "email": "string",
            "profile_pic_url": "string",
            "is_admin": true,
            "teams": [
                {
                    "team_id": "79f1972e-e7aa-404b-9b4b-ab0d9a74f1e8",
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
                "company_id": "054f288a-9917-4578-85ae-ca63e29f3535",
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

