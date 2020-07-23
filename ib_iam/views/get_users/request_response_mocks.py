


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b8b47869-7ae1-4ca6-98ef-9b2635d4ac63",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a350bd20-982d-484b-a453-6b3d2565fd31",
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
                "company_id": "7659edb7-ec6a-42d6-9a46-4588f784d4a1",
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

