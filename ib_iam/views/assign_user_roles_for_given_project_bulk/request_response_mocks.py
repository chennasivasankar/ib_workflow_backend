

REQUEST_BODY_JSON = """
{
    "users": [
        {
            "user_id": "5d4009bd-4db7-4cac-82b1-76112aa58a80",
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
    "res_status": "USER_DOES_NOT_HAVE_ACCESS"
}
"""

