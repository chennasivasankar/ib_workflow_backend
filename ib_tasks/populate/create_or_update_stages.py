from typing import Dict, Any, List


def populate_stages_values(list_of_stages_dict: List[Dict]):
    validation_for_list_of_stages_dict(list_of_stages_dict)
    stages_dtos = [append_stage_dto(stage_dict)
                   for stage_dict in list_of_stages_dict]

    from ib_tasks.interactors.create_or_update_stages \
        import CreateOrUpdateStagesInterface
    from ib_tasks.storages.tasks_storage_implementation import \
        TasksStorageImplementation
    from ib_tasks.storages.storage_implementation import \
        StagesStorageImplementation
    interactor = CreateOrUpdateStagesInterface(
        stage_storage=StagesStorageImplementation(),
        task_storage=TasksStorageImplementation()
    )
    interactor.create_or_update_stages(stages_details=stages_dtos)


def append_stage_dto(stage_dict: Dict[str, Any]):
    from ib_tasks.interactors.dtos import StageDTO
    stage_dto = StageDTO(
        stage_id=stage_dict['stage_id'],
        task_template_id=stage_dict['task_template_id'],
        value=stage_dict['value'],
        id=None,
        stage_display_name=stage_dict['stage_display_name'],
        stage_display_logic=stage_dict['stage_display_logic']
    )
    return stage_dto


def validation_for_list_of_stages_dict(stages_dict: List[Dict]):
    from schema import Schema, SchemaError

    schema = Schema(
        [{
            "task_template_id": str,
            "stage_id": str,
            "value": int,
            "stage_display_name": str,
            "stage_display_logic": str
        }]

    )

    try:
        schema.validate(stages_dict)
    except SchemaError:
        raise_exception_for_invalid_format()


def raise_exception_for_invalid_format():
    valid_format = {
        "task_template_id": "task_template_id_1",
        "stage_id": "stage_id_1",
        "value": 1,
        "stage_display_name": "stage_name",
        "stage_display_logic": "status_1==stage_id_1"
    }

    import json
    json_valid_format = json.dumps(valid_format)

    from ib_tasks.exceptions.stage_custom_exceptions import \
        InvalidFormatException
    raise InvalidFormatException(valid_format=json_valid_format)
