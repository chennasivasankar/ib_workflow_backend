

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c2321875-cf42-4e65-acce-1d2769645c09",
    "team_ids": [
        "84789084-0eb6-477d-8090-9af1c035c407"
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

