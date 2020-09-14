


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "af364a9f-72c0-4885-b04b-16f25bd93785",
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

