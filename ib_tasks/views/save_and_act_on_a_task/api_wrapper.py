from typing import List, Dict

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_tasks.interactors.task_dtos import FieldValuesDTO, SaveAndActOnTaskDTO
from .validator_class import ValidatorClass
from ...interactors.create_or_update_task.save_and_act_on_task import \
    SaveAndActOnATaskInteractor
from ...presenters.save_and_act_on_task_presenter_implementation import \
    SaveAndActOnATaskPresenterImplementation
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
    action_id = request_data['action_id']
    task_gofs = request_data['task_gofs']

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

    task_dto = SaveAndActOnTaskDTO(
        task_id=task_id,
        created_by_id=user_id,
        action_id=action_id,
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

    presenter = SaveAndActOnATaskPresenterImplementation()
    interactor = SaveAndActOnATaskInteractor(
        task_storage=task_storage, gof_storage=gof_storage,
        create_task_storage=create_task_storage,
        storage=storage, field_storage=field_storage,
        stage_storage=stage_storage
    )

    response = interactor.save_and_act_on_task_wrapper(
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
