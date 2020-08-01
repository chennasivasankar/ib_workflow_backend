


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d4d0b0d8-ee71-4e71-bf44-0ea594ea9a02",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b3623a24-e544-4eb9-9874-6acbde235171",
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
                "company_id": "b1e67fd0-b764-43cc-a661-ee827ef5b69a",
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

