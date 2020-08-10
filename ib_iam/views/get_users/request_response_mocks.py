


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "e5848d66-5b70-4acb-8462-5168ef0eb2df",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ee7402e8-2614-4e4c-b980-ddce7705ed78",
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

