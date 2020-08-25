


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "5308ff59-9e9b-4fca-a2d7-ee3f2a1687cd",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "29b6b956-10cc-4ded-80e3-999b7ca36425",
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

