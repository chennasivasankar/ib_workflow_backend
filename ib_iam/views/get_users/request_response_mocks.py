


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "2df54de5-620e-47e1-8482-4863318137e0",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "2aefac0d-4345-47c0-9e96-7207e5eb154e",
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

