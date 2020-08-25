

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "c7b5151b-01cb-43fd-bedb-c99bbe45cc3c",
    "team_ids": [
        "19f61862-f0c9-4e5d-a199-d57750d46075"
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

