


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "68a394d7-3e6a-4c78-bfff-93661dfedeca",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "53f06043-734a-4ba6-a325-ede65b6dc288",
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

