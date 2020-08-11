


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "444bcbb4-28c6-4122-91f8-4b53aa66f555",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "d84b08e9-d252-42e6-ac90-4c9ab11f4cde",
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

