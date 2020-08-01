


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "ece1f207-25ff-43a9-83fd-ef0b045d4b12",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "2ee70a6d-d149-431f-a568-d1a5e8cde95a",
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
                "company_id": "74f5b9b2-210d-4220-8b8a-32b3d08edc5a",
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

