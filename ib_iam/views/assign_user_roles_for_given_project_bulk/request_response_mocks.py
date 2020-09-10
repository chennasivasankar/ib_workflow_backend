

REQUEST_BODY_JSON = """
{
    "users": [
        {
            "user_id": "a25709e5-ebe5-4723-92c0-99b62c2960ee",
            "role_ids": [
                "string"
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
    "res_status": "USER_DOES_NOT_ACCESS"
}
"""

