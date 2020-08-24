


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "f38b6655-d5ff-4cf3-ba72-b4b93437a602",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "0d05bfbc-13f3-43aa-bd00-0a5757c4627a",
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

