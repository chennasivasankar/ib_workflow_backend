

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "670b4760-022e-4118-9aba-1007dc974ea8",
    "team_ids": [
        "df870876-80dd-4176-aa9e-67999b5a7fb4"
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

