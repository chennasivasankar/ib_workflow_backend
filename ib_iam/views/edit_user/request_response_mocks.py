

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f060fca5-d2aa-4fa5-9e55-cce20f294497",
    "team_ids": [
        "699cc360-4d65-4296-ab9d-1b925f155350"
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

