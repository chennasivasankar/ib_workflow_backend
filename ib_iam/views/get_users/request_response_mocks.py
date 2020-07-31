


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "13125f62-7e1f-4066-a839-0082b3bd0bd4",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "bfbc7644-063e-4f8d-a2ca-cdf7d451d379",
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
                "company_id": "f0f3ad61-5235-4636-90d5-c04be2c90335",
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

