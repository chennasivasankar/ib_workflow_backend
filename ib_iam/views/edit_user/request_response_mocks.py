

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "67fcf39c-52f6-4bc0-a041-796ca81fb81e",
    "team_ids": [
        "a0744761-c5c1-468e-9b7d-4742542db651"
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

