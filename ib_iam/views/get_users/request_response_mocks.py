


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "2bc085ef-d430-4c0a-8730-f9ea71a43a09",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "01ff8a24-ffac-49d7-bd1e-4ad5a011fcd1",
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

