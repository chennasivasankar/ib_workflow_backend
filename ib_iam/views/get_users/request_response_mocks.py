


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "bb1e86ca-069c-454f-a839-0b4d42ed87e0",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "26fe7757-1401-458e-9ab7-f32f2e13a371",
                    "team_name": "string"
                }
            ],
            "roles": [
                {
                    "role_id": "string",
                    "role_name": "string"
                }
            ],
            "company": {
                "company_id": "string",
                "company_name": "string"
            }
        }
    ],
    "total": 1
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_DOES_NOT_HAVE_PERMISSION"
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_LIMIT"
}
"""

