


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "string",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "2feeb374-c671-44ad-9118-1c5e867047e3",
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
                "company_id": "9ef61d7a-a8ed-49cc-bca8-1e4367e0a91b",
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

