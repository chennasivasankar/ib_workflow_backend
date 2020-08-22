


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "979caed8-0ef7-4888-b891-ebf264c48585",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "85cb5770-b229-4ee4-a78b-c118cdc91f41",
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

