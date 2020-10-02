import json
from typing import Dict, List

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_tasks.views.update_task.validator_class import ValidatorClass
from ib_tasks.interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ib_tasks.interactors.task_dtos import FieldValuesDTO, \
    StageIdWithAssigneeDTO, UpdateTaskWithTaskDisplayIdDTO
from ib_tasks.presenters.update_task_presenter import \
    UpdateTaskPresenterImplementation
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.elasticsearch_storage_implementation import \
    ElasticSearchStorageImplementation
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ib_tasks.storages.gof_storage_implementation import \
    GoFStorageImplementation
from ib_tasks.storages.storage_implementation import StorageImplementation, \
    StagesStorageImplementation
from ib_tasks.storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_id = request_data.get('task_id')
    title = request_data.get('title')
    description = request_data.get('description')
    start_datetime = request_data.get('start_datetime')
    due_datetime = request_data.get('due_datetime')
    priority = request_data.get('priority')
    task_gofs = request_data.get('task_gofs')
    stage_id = request_data.get('stage_assignee').get('stage_id')
    assignee_id = request_data.get('stage_assignee').get('assignee_id')
    assignee_team_id = request_data.get('stage_assignee').get('team_id')
    request_json = json.dumps(request_data)

    from ib_tasks.interactors.task_dtos import GoFFieldsDTO

    task_gofs_dtos = []
    for task_gof in task_gofs:
        gof_field_dto = GoFFieldsDTO(
            gof_id=task_gof['gof_id'],
            same_gof_order=task_gof['same_gof_order'],
            field_values_dtos=get_field_values_dtos(
                fields=task_gof['gof_fields']))
        task_gofs_dtos.append(gof_field_dto)

    stage_assignee = StageIdWithAssigneeDTO(
        stage_id=stage_id,
        assignee_id=assignee_id,
        team_id=assignee_team_id)

    task_dto = UpdateTaskWithTaskDisplayIdDTO(
        task_display_id=task_id, created_by_id=user_id, title=title,
        description=description, start_datetime=start_datetime,
        due_datetime=due_datetime, priority=priority,
        stage_assignee=stage_assignee,
        gof_fields_dtos=task_gofs_dtos, action_type=None)

    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    task_storage = TasksStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    storage = StorageImplementation()
    gof_storage = GoFStorageImplementation()
    field_storage = FieldsStorageImplementation()
    stage_storage = StagesStorageImplementation()
    elastic_storage = ElasticSearchStorageImplementation()
    action_storage = ActionsStorageImplementation()
    task_stage_storage = TaskStageStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()

    presenter = UpdateTaskPresenterImplementation()
    interactor = UpdateTaskInteractor(
        task_storage=task_storage, gof_storage=gof_storage,
        create_task_storage=create_task_storage,
        storage=storage, field_storage=field_storage,
        stage_storage=stage_storage,
        elastic_storage=elastic_storage,
        action_storage=action_storage,
        task_stage_storage=task_stage_storage,
        task_template_storage=task_template_storage)
    response = interactor.update_task_wrapper(
        task_dto=task_dto, presenter=presenter, request_json=request_json)
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
