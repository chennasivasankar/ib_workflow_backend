

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "e4b10c50-8235-4ce0-8a1e-686e5e1a440d",
    "team_ids": [
        "78b5aebb-0463-4b82-b0cc-5645bd14042d"
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

