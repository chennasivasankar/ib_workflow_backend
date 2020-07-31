


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "f78cdb1d-1160-41dd-bdfc-d790ec163601",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "c883a514-cff6-4659-b2ce-5082641ddace",
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
                "company_id": "18fa5ab5-31af-4eca-9776-4417d9f8141e",
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

