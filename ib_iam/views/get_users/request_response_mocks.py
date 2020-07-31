


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "435ed593-ebbc-4ca3-9b39-94889f3649b0",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ae8fcc89-5fc7-43bb-a0cd-29733aa640d4",
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
                "company_id": "bf5d3266-75b0-406f-9e57-21117bc490f3",
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

