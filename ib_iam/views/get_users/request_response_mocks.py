


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "3c7de104-c071-484f-9328-6a7270d0eda0",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "5b715461-b81e-49c5-984b-ec07201a724b",
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

