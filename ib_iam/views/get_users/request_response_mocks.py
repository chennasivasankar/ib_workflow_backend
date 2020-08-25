


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "880afb03-65b9-42ea-b3e3-d45ec83508ac",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b46f1036-c0b8-4fe0-ab7a-c667a0883f54",
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

