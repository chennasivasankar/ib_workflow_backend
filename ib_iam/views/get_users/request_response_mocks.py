


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "1ec3bb56-c9b9-45c6-8853-2d18b601b5be",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "9fa47269-c620-4da3-820b-753e38464eb6",
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

