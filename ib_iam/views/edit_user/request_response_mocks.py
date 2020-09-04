

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c49998a5-2164-4d7e-87cd-8b09102378ca",
    "team_ids": [
        "d6a22fb2-a8f3-457f-8590-4193d9020d0b"
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

