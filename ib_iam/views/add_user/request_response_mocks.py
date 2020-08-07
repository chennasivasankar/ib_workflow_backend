

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "4010df1a-857e-46eb-89ab-a8dae1df2808",
    "team_ids": [
        "51937737-3338-4d30-bcca-e688483032b8"
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

