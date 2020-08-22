from typing import Dict, List

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ...interactors.task_dtos import UpdateTaskDTO, FieldValuesDTO, \
    StageIdWithAssigneeDTO, UpdateTaskWithTaskDisplayIdDTO
from ...presenters.update_task_presenter import \
    UpdateTaskPresenterImplementation
from ...storages.elasticsearch_storage_implementation \
    import ElasticSearchStorageImplementation
from ...storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.storage_implementation import StorageImplementation, \
    StagesStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_id = request_data['task_id']
    title = request_data['title']
    description = request_data['description']
    start_date = request_data['start_date']
    due_date = request_data['due_date']['date']
    due_time = request_data['due_date']['time']
    priority = request_data['priority']
    task_gofs = request_data['task_gofs']
    stage_assignee_stage_id = request_data['stage_assignee']['stage_id']
    stage_assignee_assignee_id = request_data['stage_assignee']['assignee_id']
    assignee_team_id = request_data['stage_assignee']['team_id']

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
        stage_id=stage_assignee_stage_id,
        assignee_id=stage_assignee_assignee_id,
        team_id=assignee_team_id
    )

    task_dto = UpdateTaskWithTaskDisplayIdDTO(
        task_display_id=task_id, created_by_id=user_id, title=title,
        description=description, start_date=start_date, due_date=due_date,
        due_time=due_time, priority=priority, stage_assignee=stage_assignee,
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
    elastic_storage = ElasticSearchStorageImplementation()

    presenter = UpdateTaskPresenterImplementation()
    interactor = UpdateTaskInteractor(
        task_storage=task_storage, gof_storage=gof_storage,
        create_task_storage=create_task_storage,
        storage=storage, field_storage=field_storage,
        stage_storage=stage_storage,
        elastic_storage=elastic_storage
    )

    response = interactor.update_task_wrapper(
        task_dto=task_dto, presenter=presenter)
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
