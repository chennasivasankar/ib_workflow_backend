

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "8d63cbd8-e27b-42aa-b64b-41a30dd2ec08",
    "team_ids": [
        "1cf857f1-fc3c-4cde-84f9-bb90dcc968de"
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

