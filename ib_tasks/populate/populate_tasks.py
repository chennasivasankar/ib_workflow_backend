from typing import Dict, Any, List


def populate_tasks(tasks: List[Dict]):
    tasks_dto = []
    validation_for_tasks_dict(tasks)
    for action_dict in tasks:
        tasks_dto.append(append_action_dict(action_dict))
    return tasks_dto


def append_action_dict(action_dict: Dict[str, Any]):
    from ib_tasks.interactors.dtos import TaskTemplateStageActionDTO
    return TaskTemplateStageActionDTO(
        task_template_id=action_dict['task_template_id'],
        stage_id=action_dict['stage_id'],
        action_name=action_dict['action_name'],
        logic=action_dict['action_logic'],
        role=action_dict['role'],
        button_text=action_dict['button_text'],
        button_color=action_dict.get("button_color")
    )


def validation_for_tasks_dict(tasks_dict: List[Dict]):

    from schema import Schema, Optional, SchemaError
    schema = Schema(
        [{
            "task_template_id": str,
            "stage_id": str,
            "action_logic": str,
            "action_name": str,
            "role": str,
            "button_text": str,
            Optional("button_color"): str
        }]
    )
    try:
        schema.validate(tasks_dict)
    except SchemaError:
        raise_exception_for_valid_format()


def raise_exception_for_valid_format():
    valid_format = {
        "task_template_id": "task_template_1",
        "stage_id": "stage_1",
        "action_logic": "logic_1",
        "action_name": "action_name_1",
        "roles": "ROLE_1",
        "button_text": "button_text_1",
        "button_color": "button_color_1"
    }
    import json
    json_valid_format = json.dumps(valid_format)
    from ib_tasks.exceptions.custom_exceptions \
        import InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
