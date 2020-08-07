


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "3eca91b2-795f-4c80-938d-ea6e8402afbf",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "dc0ee211-fde5-499d-84f1-65ba730a9515",
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

