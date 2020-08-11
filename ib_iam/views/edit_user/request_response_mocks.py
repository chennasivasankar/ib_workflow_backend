

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "692b0ce9-df6e-4dcc-9380-c619a918834a",
    "team_ids": [
        "335b2f20-f7e0-4cad-88a8-c08cfaf3d499"
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

