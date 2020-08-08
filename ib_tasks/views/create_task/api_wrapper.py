from typing import List, Dict

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_tasks.interactors.task_dtos import FieldValuesDTO
from .validator_class import ValidatorClass
from ...presenters.create_task_presenter import \
    CreateTaskPresenterImplementation
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.storage_implementation import StorageImplementation, \
    StagesStorageImplementation
from ...storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_template_id = request_data['task_template_id']
    action_id = request_data['action_id']
    title = request_data.get('title', 'Task')
    description = request_data.get('description', 'description')
    import datetime
    start_date = request_data.get('start_date', datetime.date(year=2020, month=8, day=8))
    due_date = request_data.get('due_date', {"date": datetime.date(year=2020, month=8, day=9), "time": "12:30:00"})['date']
    due_time = request_data.get('due_date', {"date": "2020-08-08", "time": "12:00:00"})['time']
    priority = request_data.get('priority', 'HIGH')
    task_gofs = request_data['task_gofs']

    from ib_tasks.interactors.task_dtos import GoFFieldsDTO, CreateTaskDTO

    task_gofs_dtos = []
    for task_gof in task_gofs:
        gof_field_dto = GoFFieldsDTO(
            gof_id=task_gof['gof_id'],
            same_gof_order=task_gof['same_gof_order'],
            field_values_dtos=get_field_values_dtos(
                fields=task_gof['gof_fields'])
        )
        task_gofs_dtos.append(gof_field_dto)

    task_dto = CreateTaskDTO(
        task_template_id=task_template_id, created_by_id=user_id,
        action_id=action_id, title=title, description=description,
        start_date=start_date, due_date=due_date, due_time=due_time,
        priority=priority, gof_fields_dtos=task_gofs_dtos
    )

    from ib_tasks.storages.tasks_storage_implementation \
        import TasksStorageImplementation
    from ib_tasks.storages.create_or_update_task_storage_implementation \
        import CreateOrUpdateTaskStorageImplementation
    from ib_tasks.interactors.create_or_update_task.create_task_interactor \
        import CreateTaskInteractor
    from ib_tasks.storages.elasticsearch_storage_implementation \
        import ElasticSearchStorageImplementation
    task_storage = TasksStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    storage = StorageImplementation()
    field_storage = FieldsStorageImplementation()
    stage_storage = StagesStorageImplementation()
    gof_storage = GoFStorageImplementation()
    task_template_storage = TaskTemplateStorageImplementation()
    action_storage = ActionsStorageImplementation()
    presenter = CreateTaskPresenterImplementation()
    elastic_storage = ElasticSearchStorageImplementation()

    interactor = CreateTaskInteractor(
        task_storage=task_storage,
        create_task_storage=create_task_storage,
        storage=storage, field_storage=field_storage,
        stage_storage=stage_storage, gof_storage=gof_storage,
        task_template_storage=task_template_storage,
        action_storage=action_storage,
        elastic_storage=elastic_storage
    )

    response = interactor.create_task_wrapper(
        task_dto=task_dto, presenter=presenter
    )
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
