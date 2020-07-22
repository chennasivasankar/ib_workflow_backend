

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
    "company_id": "1a8d8913-c861-49ce-9630-87edd189f38f"
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

