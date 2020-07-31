

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "21c1d067-a722-4f36-aa0d-4298c7035d53",
    "team_ids": [
        "196423f8-4de5-4384-9444-752e44a628ab"
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

