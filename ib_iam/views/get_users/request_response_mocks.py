


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "2f8a831d-80c1-4592-a702-1ae457b90021",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "087b5137-977e-443b-a024-0c4d86a09a02",
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
                "company_id": "725a77db-4572-4a35-8961-d05f99f1a72b",
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

