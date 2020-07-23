

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "logo_url": "string",
    "user_ids": [
        "string"
    ]
}
"""


RESPONSE_201_JSON = """
{
    "company_id": "817352bd-c0d7-42ee-a79b-7bb955f96e82"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "COMPANY_NAME_ALREADY_EXISTS"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USERS"
}
"""

