


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4e8deff5-1ac7-4e76-9cc0-795040e4c7d1",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "e92c88e9-c478-43c0-9a6b-eb936f8bed5e",
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
                "company_id": "e5c8155b-8a6f-4573-ab7e-a8fd44acc7a7",
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

