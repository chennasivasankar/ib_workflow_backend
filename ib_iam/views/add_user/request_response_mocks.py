

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "594500e4-034e-4d3e-ab6b-4a859467b2d3",
    "team_ids": [
        "6155e3e8-c2e8-4320-9f5c-907e0ca229ac"
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

