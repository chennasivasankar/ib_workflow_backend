


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "f8235e3d-0cca-4ffa-9deb-b3577789db61",
            "name": "string",
            "email": "string",
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "teams": [
                {
                    "team_id": "21880cf8-f096-4d64-960f-9e54c71db9ba",
                    "team_name": "string"
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

