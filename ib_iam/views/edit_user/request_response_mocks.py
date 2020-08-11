

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ae4dc505-9d65-4e35-80f0-8a4b13bc2b73",
    "team_ids": [
        "2387bde5-9381-4123-ab04-2dabca6feb6a"
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

