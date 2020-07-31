

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "395ecc08-2323-41cd-a80d-b60d8aec1966",
    "team_ids": [
        "83991e59-912a-49da-9add-834f02208976"
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

