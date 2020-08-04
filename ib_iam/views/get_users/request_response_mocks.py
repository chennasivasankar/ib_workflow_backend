


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "9e4885c8-1143-46e8-b030-546ef362665e",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "3a9a6c04-9cad-4728-9334-f0c192bec2bb",
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
                "company_id": "04c76ef4-53d2-427e-bf62-96376d903ae2",
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

