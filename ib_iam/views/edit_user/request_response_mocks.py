

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "3f409db7-abe3-4868-aa6c-b700eb61d29f",
    "team_ids": [
        "2b0e39c1-5725-4420-bb43-5c68ff1533e1"
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

