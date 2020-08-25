


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "e2145a1c-3c95-44ef-877b-904a277244ac",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "42968be8-e537-4e61-a68e-e609124c9499",
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

