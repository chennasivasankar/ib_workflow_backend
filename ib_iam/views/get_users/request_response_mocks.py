


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "5e3f7627-2bf8-45f7-9272-9a4c11ded041",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "3ddbd2b8-a759-46d6-94ab-0e7f593430e1",
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

