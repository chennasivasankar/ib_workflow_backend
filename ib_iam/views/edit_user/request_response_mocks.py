

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c464f642-65ba-4dc9-a85a-195ca4d81615",
    "team_ids": [
        "8589fee5-e6c7-4bfa-af24-1098473d6bb5"
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

