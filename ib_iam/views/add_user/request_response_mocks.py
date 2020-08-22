

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "377aa3af-cbf7-44e9-9597-469cdf58ecc4",
    "team_ids": [
        "6dc9b58b-03c4-48ec-a45f-2ae8a98858bc"
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

