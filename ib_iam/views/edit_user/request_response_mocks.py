

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "bb20ecac-6eaf-4ab3-9589-1bbb1dce20f4",
    "team_ids": [
        "57391087-590e-4bca-8f58-bac25263755f"
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

