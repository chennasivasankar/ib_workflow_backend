


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "459ff345-47a7-4cfe-bd70-54686f2fd70a",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "11864be9-da6b-453b-b63f-1fd84af7d02c",
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

