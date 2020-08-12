

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b0cb3153-dcdc-4df5-870f-01c80a7a55f1",
    "team_ids": [
        "97b25c4c-9e64-445a-9696-062558cad511"
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

