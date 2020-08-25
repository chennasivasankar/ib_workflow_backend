


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "c7fb7a8b-eddb-44a1-a383-de639245fec7",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "8b93f3aa-53e8-495e-8695-706d1242555b",
                    "team_name": "string"
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

