


RESPONSE_200_JSON = """
[
    {
        "template_id": "string",
        "project_id": "string",
        "template_name": "string",
        "actions": [
            {
                "action_id": 1,
                "action_type": "NO_VALIDATIONS",
                "transition_template_id": "string",
                "button_text": "string",
                "button_color": "string"
            }
        ],
        "group_of_fields": [
            {
                "gof_id": "string",
                "gof_display_name": "string",
                "max_columns": 1,
                "order": 1,
                "enable_add_another": true,
                "fields": [
                    {
                        "field_type": "PLAIN_TEXT",
                        "field_id": "string",
                        "display_name": "string",
                        "is_field_required": true,
                        "field_values": "string",
                        "allowed_formats": "string",
                        "validation_regex": "string",
                        "error_msg": "string",
                        "tooltip": "string",
                        "help_text": "string",
                        "placeholder_text": "string",
                        "is_field_writable": true,
                        "order": 1
                    }
                ]
            }
        ]
    }
]
"""

RESPONSE_404_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "TASK_TEMPLATES_DOES_NOT_EXISTS"
}
"""

