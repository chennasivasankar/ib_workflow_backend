

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "116e80b0-8d94-4933-8c79-e6c4677dac2d",
    "team_ids": [
        "b4fae262-cba6-4c70-a5f9-a8f1de79f3d1"
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

