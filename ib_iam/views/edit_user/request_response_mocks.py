

REQUEST_BODY_JSON = """
{
    "name": "string",
    "email": "string",
    "company_id": "f989b5fd-20ac-46eb-ae8e-7cbf53a533dc",
    "team_ids": [
        "5b9ca959-a139-4305-880d-69fe83f13369"
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

