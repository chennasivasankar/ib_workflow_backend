import json
from typing import List, Dict

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_tasks.interactors.task_dtos import FieldValuesDTO, \
    StageIdWithAssigneeDTO, SaveAndActOnTaskWithTaskDisplayIdDTO
from .validator_class import ValidatorClass
from ...interactors.create_or_update_task.save_and_act_on_task import \
    SaveAndActOnATaskInteractor
from ...presenters.save_and_act_on_task_presenter_implementation import \
    SaveAndActOnATaskPresenterImplementation
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.elasticsearch_storage_implementation import \
    ElasticSearchStorageImplementation
from ...storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.storage_implementation import StorageImplementation, \
    StagesStorageImplementation
from ...storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ...storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_id = request_data.get('task_id')
    action_id = request_data.get('action_id')
    title = request_data.get('title')
    description = request_data.get('description')
    start_datetime = request_data.get('start_datetime')
    due_datetime = request_data.get('due_datetime')
    priority = request_data.get('priority')
    task_gofs = request_data.get('task_gofs')
    stage_id = request_data.get('stage_assignee').get('stage_id')
    assignee_id = request_data.get('stage_assignee').get('assignee_id')
    assignee_team_id = request_data.get('stage_assignee').get('team_id')
    request_data['start_datetime'] = str(start_datetime)
    request_data['due_datetime'] = str(due_datetime)
    task_request_json = json.dumps(request_data)

    from ib_tasks.interactors.task_dtos import GoFFieldsDTO

    task_gofs_dtos = []
    for task_gof in task_gofs:
        gof_field_dto = GoFFieldsDTO(
            gof_id=task_gof['gof_id'],
            same_gof_order=task_gof['same_gof_order'],
            field_values_dtos=get_field_values_dtos(
                fields=task_gof['gof_fields'])
        )
        task_gofs_dtos.append(gof_field_dto)

    stage_assignee = StageIdWithAssigneeDTO(
        stage_id=stage_id,
        assignee_id=assignee_id,
        team_id=assignee_team_id
    )

    task_dto = SaveAndActOnTaskWithTaskDisplayIdDTO(
        task_display_id=task_id, action_id=action_id, created_by_id=user_id,
        title=title,
        description=description, start_datetime=start_datetime,
        due_datetime=due_datetime, priority=priority,
        stage_assignee=stage_assignee,
        gof_fields_dtos=task_gofs_dtos
    )

    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import \
        CreateOrUpdateTaskStorageImplementation
    task_storage = TasksStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    storage = StorageImplementation()
    gof_storage = GoFStorageImplementation()
    field_storage = FieldsStorageImplementation()
    stage_storage = StagesStorageImplementation()
    action_storage = ActionsStorageImplementation()
    elastic_storage = ElasticSearchStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()

    presenter = SaveAndActOnATaskPresenterImplementation()
    interactor = SaveAndActOnATaskInteractor(
        task_storage=task_storage, gof_storage=gof_storage,
        create_task_storage=create_task_storage,
        storage=storage, field_storage=field_storage,
        stage_storage=stage_storage, action_storage=action_storage,
        elastic_storage=elastic_storage, task_stage_storage=task_stage_storage,
        task_template_storage=task_template_storage
    )

    response = interactor.save_and_act_on_task_wrapper(
        task_dto=task_dto, presenter=presenter,
        task_request_json=task_request_json)
    return response


def get_field_values_dtos(fields: List[Dict]) -> List[FieldValuesDTO]:
    field_values_dtos = [
        FieldValuesDTO(
            field_id=field['field_id'],
            field_response=field['field_response']
        )
        for field in fields
    ]
    return field_values_dtos
