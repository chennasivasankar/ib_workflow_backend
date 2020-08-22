


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "6219128c-a29c-4240-9d24-815d7af30245",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "205fbc05-6d58-46f9-aa9e-55bfd0d0d8dc",
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

