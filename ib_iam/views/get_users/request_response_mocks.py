


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "030ea32e-7767-4846-8599-8b059a06c912",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bbafe32c-8c9e-45e7-8bed-aec46b6f9a37",
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

