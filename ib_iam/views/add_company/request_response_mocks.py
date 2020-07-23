

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
    "company_id": "fec2b2b8-cd85-4650-bbec-41a4d8482e94"
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

