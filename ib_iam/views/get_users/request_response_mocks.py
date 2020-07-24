


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "66b19d9e-a400-48c2-8d5d-c1068a9740d9",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4bbd3e86-814d-4e56-bc7b-71ab01c87039",
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
                "company_id": "10d23a19-5feb-4d02-9d4c-613d00c6ec75",
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

