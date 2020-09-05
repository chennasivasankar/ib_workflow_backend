

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "9d145ba7-089a-47aa-823c-a0fe48b31538",
    "team_ids": [
        "f0fa5331-11e1-4926-9354-34b04275414d"
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

