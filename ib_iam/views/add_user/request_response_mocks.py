

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4a893bbe-4f7c-4b4e-b7b9-90dd478e3c52",
    "team_ids": [
        "7ebc9801-055e-4147-8fff-163999e39eae"
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

