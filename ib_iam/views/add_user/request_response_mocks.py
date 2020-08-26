

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "5cb35bf7-15c8-4e63-a88e-b4117d79a575",
    "team_ids": [
        "e51649bc-5328-4c4e-aaab-636d342b3a56"
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

