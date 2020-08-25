

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "34ad861e-95ba-4a03-8372-e1baccd8f12e",
    "team_ids": [
        "41662709-ab68-45f2-8c33-c9cd133b2a65"
    ]
}
"""


RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_EMAIL"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_COMPANY_ID"
}
"""

