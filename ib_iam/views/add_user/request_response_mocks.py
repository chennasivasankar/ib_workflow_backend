

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "ce70c2e8-21bb-427e-9d78-d7770a94bf18",
    "team_ids": [
        "41467e10-cef5-4ccb-b157-ff6d1d870690"
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

