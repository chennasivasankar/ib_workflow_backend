

REQUEST_BODY_JSON = """
{
    "name": "string",
    "description": "string",
    "logo_url": "string",
    "employee_ids": [
        "string"
    ]
}
"""


RESPONSE_201_JSON = """
{
    "company_id": "cd9446af-9f62-410c-a14d-02ecebbc91af"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "COMPANY_NAME_ALREADY_EXISTS"
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USER_IDS"
}
"""

