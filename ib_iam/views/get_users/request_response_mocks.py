


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "ff885619-91d2-4857-b57a-509fdbc1e660",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "51903717-f472-42df-ac00-b0a4e0350335",
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

