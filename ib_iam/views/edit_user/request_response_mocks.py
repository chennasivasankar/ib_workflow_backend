

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f2f20b70-f3eb-4f14-a212-6021782dab25",
    "team_ids": [
        "6e8e7ac0-2cfa-4135-923e-d5bef68f0b61"
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

