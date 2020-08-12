

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8ae87044-a3b5-45c5-8450-d73136a469f1",
    "team_ids": [
        "91e8863f-cbaf-4d91-8dcb-098790454917"
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

