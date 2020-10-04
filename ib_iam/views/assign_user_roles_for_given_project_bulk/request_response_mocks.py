

REQUEST_BODY_JSON = """
{
    "users": [
        {
            "user_id": "27d7b750-8625-4bfc-98d7-8a5156e9cbd2",
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

