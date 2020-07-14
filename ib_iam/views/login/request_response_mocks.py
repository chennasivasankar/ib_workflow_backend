

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
    "expires_in": "2099-12-31 00:00:00"
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

