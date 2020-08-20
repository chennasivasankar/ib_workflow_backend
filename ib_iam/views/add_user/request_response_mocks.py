

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "44370314-ab88-4be0-98cb-66ef25d26abf",
    "team_ids": [
        "f552abaf-a00e-45d5-90bc-78eab6adc8d1"
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

