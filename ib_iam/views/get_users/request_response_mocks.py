


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9aad5d1c-99a9-43f4-a9b4-8565158ad3ad",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ef5ed7c9-baeb-4734-9690-47b062cdaf0e",
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
                "company_id": "adde7533-c3bc-4973-8505-d7dd0bdde524",
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

