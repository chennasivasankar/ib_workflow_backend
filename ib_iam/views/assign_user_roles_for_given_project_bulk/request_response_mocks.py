

REQUEST_BODY_JSON = """
{
    "users": [
        {
            "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09",
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

