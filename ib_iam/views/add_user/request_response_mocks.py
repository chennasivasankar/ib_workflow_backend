

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9efcb5d8-a42d-44ba-89ec-2da0e116778c",
    "team_ids": [
        "20e5ca9d-662d-4984-8ccf-6b35a120c713"
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

