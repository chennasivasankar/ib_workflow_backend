


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "33671419-f30a-4eb7-94f5-9536bb4d3392",
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
                    "team_id": "abb11f1f-5c0c-4310-8cb5-037b1f681b3b",
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

