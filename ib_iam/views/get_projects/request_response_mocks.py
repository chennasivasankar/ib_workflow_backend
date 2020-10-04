


RESPONSE_200_JSON = """
{
    "total_projects_count": 1,
    "projects": [
        {
            "name": "string",
            "description": "string",
            "logo_url": "string",
            "project_id": "string",
            "project_display_id": "string",
            "teams": [
                {
                    "team_id": "8a376d8d-fb86-4489-a79c-50f049809f06",
                    "team_name": "string"
                }
            ],
            "roles": [
                {
                    "role_name": "string",
                    "description": "string",
                    "role_id": "string"
                }
            ]
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_OFFSET_VALUE"
}
"""

RESPONSE_403_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "USER_HAS_NO_ACCESS_TO_GET_PROJECTS"
}
"""

