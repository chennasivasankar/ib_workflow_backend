


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
                    "team_id": "7178e698-a4c0-4997-ae52-313ac189621a",
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
                "company_id": "283450d6-54cf-4843-a520-f11fdae2fce3",
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

