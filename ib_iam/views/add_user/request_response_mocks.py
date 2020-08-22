

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d2a57d2e-a67d-4f15-a5cf-ac856e995128",
    "team_ids": [
        "cb57af64-280c-4b4a-a7cc-e28acc361888"
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

