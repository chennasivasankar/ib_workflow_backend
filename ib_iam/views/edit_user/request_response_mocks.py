

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "b19753dd-1980-4861-bbce-c4477aa836c3",
    "team_ids": [
        "a936f824-7315-4809-8b7c-7fa59d7cc73e"
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

