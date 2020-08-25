

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a66d6b89-f101-4337-bd32-b53652476e30",
    "team_ids": [
        "17be565f-2062-4ad6-8ca2-64d20f657980"
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

