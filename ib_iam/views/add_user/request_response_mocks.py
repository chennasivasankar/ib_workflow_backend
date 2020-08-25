

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "1bf44a2d-75fb-4f59-b95f-83e453395d46",
    "team_ids": [
        "4f339748-89ed-454d-bfd5-df68ac8aec69"
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

