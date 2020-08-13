

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "a660b02b-84df-4413-9f0c-6e745c4025e6",
    "team_ids": [
        "75dd5442-033f-4c16-abe8-6090f8d8de45"
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

