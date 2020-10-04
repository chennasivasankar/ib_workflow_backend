

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "38a603f6-a917-4ec8-b1ee-fbd36884825a",
    "team_ids": [
        "ba99f809-e76b-46dc-b633-a126239e1996"
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

