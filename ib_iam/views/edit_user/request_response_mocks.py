

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f43a9418-a441-4b78-929f-7951686a8945",
    "team_ids": [
        "577bcc6f-383f-4c41-8295-01680d634eae"
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

