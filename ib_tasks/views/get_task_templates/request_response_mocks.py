


RESPONSE_200_JSON = """
{
    "task_templates": [
        {
            "template_id": "string",
            "template_name": "string",
            "actions": [
                {
                    "action_id": "string",
                    "action_name": "string",
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
                    "enable_multiple_gofs": true,
                    "is_gof_readable": true,
                    "is_gof_writable": true,
                    "fields": [
                        {
                            "field_id": "string",
                            "display_name": "string",
                            "is_field_required": true,
                            "field_type": "PLAIN_TEXT",
                            "field_values": "string",
                            "allowed_formats": "string",
                            "validation_regex": "string",
                            "error_msg": "string",
                            "tooltip": "string",
                            "help_text": "string",
                            "placeholder_text": "string",
                            "is_field_readable": true,
                            "is_field_writable": true
                        }
                    ]
                }
            ]
        }
    ]
}
"""

