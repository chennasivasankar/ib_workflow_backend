

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f07a0548-5073-4f99-8077-08afdc00f3a9",
    "team_ids": [
        "efd9b6e5-ee19-4538-8de6-8de73837d108"
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

