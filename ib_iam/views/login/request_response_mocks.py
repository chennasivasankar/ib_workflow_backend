

REQUEST_BODY_JSON = """
{
    "email": "string",
    "password": "string"
}
"""


RESPONSE_200_JSON = """
{
    "access_token": "string",
    "refresh_token": "string",
    "expires_in_seconds": 1
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "InvalidEmail"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "InvalidPassword"
}
"""

