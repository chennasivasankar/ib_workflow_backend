

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "04ffb20e-cad2-4731-b073-1efe65374f3b",
    "team_ids": [
        "ac4077f3-6189-4e65-ae79-bcab268c3be3"
    ],
    "role_ids": [
        "string"
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

