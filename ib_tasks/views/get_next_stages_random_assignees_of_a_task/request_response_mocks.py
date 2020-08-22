

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "action_id": "string"
}
"""


RESPONSE_200_JSON = """
{
    "stage_assignees": [
        {
            "stage_id": 1,
            "stage_display_name": "string",
            "assignee": {
                "assignee_id": "string",
                "name": "string",
                "profile_pic_url": "string",
                "team_info": {
                    "team_id": "string",
                    "team_name": "string"
                }
            }
        }
    ]
}
"""

RESPONSE_400_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_TASK_ID"
}
"""

