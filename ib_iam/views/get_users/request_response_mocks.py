


RESPONSE_200_JSON = """
{
    "users": [
        {
            "user_id": "d281a05b-70f0-4eb9-83f9-c136ffb6768d",
            "name": "string",
            "email": "string",
            "teams": [
                {
                    "team_id": "b71dcd5f-1f52-43d8-8d3a-0055fb3a5239",
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
                "company_id": "271caa17-78b0-4813-a71d-c0370e3a03a5",
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

