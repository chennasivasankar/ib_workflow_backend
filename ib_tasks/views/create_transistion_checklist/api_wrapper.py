from typing import List, Dict

from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass
from ...interactors.create_transition_checklist_template import \
    CreateTransitionChecklistTemplateInteractor
from ...interactors.task_dtos import GoFFieldsDTO, FieldValuesDTO
from ...interactors.task_template_dtos import \
    CreateTransitionChecklistTemplateWithTaskDisplayIdDTO
from ...presenters.create_transition_checklist_presenter import \
    CreateTransitionChecklistTemplatePresenterImplementation
from ...storages.action_storage_implementation import \
    ActionsStorageImplementation
from ...storages.create_or_update_task_storage_implementation import \
    CreateOrUpdateTaskStorageImplementation
from ...storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ...storages.gof_storage_implementation import GoFStorageImplementation
from ...storages.storage_implementation import StorageImplementation
from ...storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ...storages.tasks_storage_implementation import TasksStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = kwargs['user'].user_id
    request_data = kwargs['request_data']
    task_id = request_data['task_id']
    transition_checklist_template_id = request_data[
        'transition_checklist_template_id']
    action_id = request_data['action_id']
    stage_id = request_data['stage_id']
    transition_checklist_gofs = request_data['transition_checklist_gofs']
    transition_checklist_gof_dtos = []
    for transition_checklist_gof in transition_checklist_gofs:
        gof_field_dto = GoFFieldsDTO(
            gof_id=transition_checklist_gof['gof_id'],
            same_gof_order=transition_checklist_gof['same_gof_order'],
            field_values_dtos=get_field_values_dtos(
                fields=transition_checklist_gof['gof_fields'])
        )
        transition_checklist_gof_dtos.append(gof_field_dto)
    transition_template_dto = \
        CreateTransitionChecklistTemplateWithTaskDisplayIdDTO(
        task_display_id=task_id, created_by_id=user_id,
        transition_checklist_template_id=transition_checklist_template_id,
        action_id=action_id, stage_id=stage_id,
        transition_checklist_gofs=transition_checklist_gof_dtos
    )

    task_storage = TasksStorageImplementation()
    create_task_storage = CreateOrUpdateTaskStorageImplementation()
    storage = StorageImplementation()
    gof_storage = GoFStorageImplementation()
    field_storage = FieldsStorageImplementation()
    template_storage = TaskTemplateStorageImplementation()
    stage_action_storage = ActionsStorageImplementation()

    presenter = CreateTransitionChecklistTemplatePresenterImplementation()

    interactor = CreateTransitionChecklistTemplateInteractor(
        create_or_update_task_storage=create_task_storage,
        template_storage=template_storage, task_storage=task_storage,
        gof_storage=gof_storage, storage=storage, field_storage=field_storage,
        stage_action_storage=stage_action_storage
    )
    interactor.create_transition_checklist_wrapper(
        transition_template_dto, presenter
    )


def get_field_values_dtos(fields: List[Dict]) -> List[FieldValuesDTO]:
    field_values_dtos = [
        FieldValuesDTO(
            field_id=field['field_id'],
            field_response=field['field_response']
        )
        for field in fields
    ]
    return field_values_dtos
