


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "e5a3c747-c937-4bcc-80dd-901d32a8dd07",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "48191a6b-fd39-41da-b07d-afa6fa778625",
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
                "company_id": "1f60513d-a2c8-4fd9-bc72-ce5665d70b94",
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

