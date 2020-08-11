


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b188f0ea-f94d-48d2-bf49-61d1330b9cea",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8a361f43-416c-498b-b453-fc0738cbc0cd",
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

