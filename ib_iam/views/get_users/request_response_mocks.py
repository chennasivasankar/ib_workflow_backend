


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "20acc7dc-cbc4-40a8-8af8-badfd15f2ce8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "a6c0f63a-97e6-43f9-b5e0-156a5f7cdf3b",
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
                "company_id": "a7a63e8f-9a38-473e-900e-80e01739cbbb",
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

