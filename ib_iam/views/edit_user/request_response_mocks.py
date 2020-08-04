

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "70f83bd5-e9b5-41f7-ae3e-37098f9588cd",
    "team_ids": [
        "5339e32f-bfff-4d99-a836-3c94c489d6bf"
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

