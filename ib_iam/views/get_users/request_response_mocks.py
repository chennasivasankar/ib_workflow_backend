


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4775970f-b9d3-4920-b9b5-0914fb0d5b7d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "dae8ea58-10d1-4628-8eb7-1692529b0115",
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

