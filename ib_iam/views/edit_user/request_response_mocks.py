

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "59d51800-b885-4e47-b17d-ea2a07852894",
    "team_ids": [
        "41988f46-56fd-4c6d-a070-b95697b35519"
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

