


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4f3386d4-3b92-45a1-9b9e-982ff6d5dc27",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8ce0aa42-d521-4a56-86a6-e46e6048a799",
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
                "company_id": "53f66297-b0c1-4769-9599-8959816b670c",
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

