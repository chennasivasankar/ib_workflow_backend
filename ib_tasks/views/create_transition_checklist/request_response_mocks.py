

REQUEST_BODY_JSON = """
{
    "task_id": "string",
    "transition_checklist_template_id": "string",
    "action_id": 1,
    "stage_id": 1,
    "transition_checklist_gofs": [
        {
            "gof_id": "string",
            "same_gof_order": 1,
            "gof_fields": [
                {
                    "field_id": "string",
                    "field_response": "string"
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
    "res_status": "string"
}
"""
