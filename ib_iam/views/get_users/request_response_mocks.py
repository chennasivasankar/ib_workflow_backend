


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "b299d8c9-1836-4d79-a799-ef7a7a0286f4",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "35027ce0-9c80-4f4c-9448-0dd6948fbf67",
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

