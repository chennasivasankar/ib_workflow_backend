


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "96eb57de-e84b-4725-accf-a04ec90c9dd8",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "ffe60ce8-52ed-4210-a072-238f8f97e203",
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

