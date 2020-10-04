


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "4f559d77-50fa-450a-9f45-067649cb8e8b",
            "name": "string",
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ]
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_PROJECT_ID"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES"
}
"""

