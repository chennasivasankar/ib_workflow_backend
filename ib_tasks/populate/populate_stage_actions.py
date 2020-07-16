from typing import Dict, Any, List


def populate_stage_actions(actions_dict: List[Dict]):
    actions_dto = []
    validation_for_action_dict(actions_dict)
    writing_data_to_task_actions_logic(actions_dict)
    for action_dict in actions_dict:
        actions_dto.append(append_action_dict(action_dict))
    return actions_dto


def writing_data_to_task_actions_logic(actions_dict: List[Dict]):
    with open('ib_tasks/populate/stage_actions_logic.py', "a") as file:
        for action_dict in actions_dict:
            _define_single_method(file=file, action_dict=action_dict)
        file.close()


def _define_single_method(file, action_dict: Dict[str, str]):
    stage_id = action_dict["stage_id"]
    action_name = action_dict["action_name"]
    action_logic = action_dict['action_logic']
    file.write(f"\n\ndef {stage_id}_{action_name}(task_dict):\n")
    file.write(action_logic + "\n")
    file.write("\t" + "return task_dict\n")


def _validate_action_logic(action_logic: str):
    from astroid import parse, AstroidSyntaxError
    from ib_tasks.exceptions.custom_exceptions \
        import InvalidPythonCodeException
    try:
        parse(action_logic)
    except AstroidSyntaxError:
        raise InvalidPythonCodeException()


def append_action_dict(action_dict: Dict[str, Any]):
    from ib_tasks.interactors.dtos import StageActionDTO

    return StageActionDTO(
        stage_id=action_dict['stage_id'],
        action_name=action_dict['action_name'],
        logic=action_dict['action_logic'],
        role=action_dict['role'],
        button_text=action_dict['button_text'],
        button_color=action_dict.get("button_color")
    )


def validation_for_action_dict(actions_dict: List[Dict]):
    from schema import Schema, Optional, SchemaError
    schema = Schema(
        [{
            "stage_id": str,
            "action_logic": str,
            "action_name": str,
            "role": str,
            "button_text": str,
            Optional("button_color"): str
        }]
    )
    try:
        schema.validate(actions_dict)
    except SchemaError:
        raise_exception_for_valid_format()
    for action_dict in actions_dict:
        _validate_action_logic(action_logic=action_dict['action_logic'])


def raise_exception_for_valid_format():
    valid_format = {
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
