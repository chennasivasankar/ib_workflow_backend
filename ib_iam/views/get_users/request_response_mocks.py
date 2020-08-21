


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "fdc488de-ebae-4fc1-ba7e-d7cd3be0edd2",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "0e239ee0-7e67-41d5-b9d9-473d7297dd05",
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

