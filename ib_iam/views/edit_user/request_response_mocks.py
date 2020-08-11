

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "1a1b3736-5a69-4cb0-8305-36dd1a3bfbba",
    "team_ids": [
        "7fba6535-4ec9-4ab2-b94d-8810837cdf41"
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

