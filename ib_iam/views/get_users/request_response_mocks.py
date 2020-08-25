


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "70b9b788-9299-4e8e-afb8-3810c55e6fb9",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "4eeb1737-993f-4438-8494-bb507f740982",
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

