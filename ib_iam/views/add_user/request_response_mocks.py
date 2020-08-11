

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "23dd9e39-5759-42c8-a2af-163eb2a9f615",
    "team_ids": [
        "af817dcb-790d-4b47-8468-264bdc06ee32"
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

