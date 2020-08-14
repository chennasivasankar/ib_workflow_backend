

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "82db3235-8fc1-4fa5-b53b-4a9d3cc18da7",
    "team_ids": [
        "2443424e-b4cd-4861-a146-0fab89e4749f"
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

