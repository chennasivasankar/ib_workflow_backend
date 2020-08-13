

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "50e3b6e8-94d2-441b-960b-7637bc657477",
    "team_ids": [
        "d9007941-abc1-4f29-8635-6ae961e01a42"
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

