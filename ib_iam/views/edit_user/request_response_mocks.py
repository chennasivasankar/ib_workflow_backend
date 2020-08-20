

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "d55c33fd-f04b-4e8f-aba8-d8f2f0089950",
    "team_ids": [
        "63e5cc24-7e73-4cdb-a886-765553bc5158"
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

