

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9012bc9d-77f7-404e-952d-0b1654d3e84e",
    "team_ids": [
        "077fe200-595e-4876-ac57-043f7f9437cf"
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

