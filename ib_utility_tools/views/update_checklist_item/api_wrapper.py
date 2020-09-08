from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_utility_tools.interactors.storage_interfaces.dtos import (
    ChecklistItemWithIdDTO
)
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    checklist_item_with_id_dto = prepare_checklist_item_with_id_dto(
        request_data=request_data, kwargs=kwargs)

    from ib_utility_tools.storages.checklist_storage_implementation import \
        ChecklistStorageImplementation
    from ib_utility_tools.presenters. \
        update_checklist_item_presenter_implementation import \
        UpdateChecklistItemPresenterImplementation
    from ib_utility_tools.interactors.update_checklist_item_interactor import \
        UpdateChecklistItemInteractor
    checklist_storage = ChecklistStorageImplementation()
    presenter = UpdateChecklistItemPresenterImplementation()
    interactor = UpdateChecklistItemInteractor(
        checklist_storage=checklist_storage)

    response_data = interactor.update_checklist_item_wrapper(
        checklist_item_with_id_dto=checklist_item_with_id_dto,
        presenter=presenter)
    return response_data


def prepare_checklist_item_with_id_dto(
        request_data, kwargs
) -> ChecklistItemWithIdDTO:
    checklist_item_with_entity_dto = ChecklistItemWithIdDTO(
        checklist_item_id=kwargs["checklist_item_id"],
        text=request_data["text"], is_checked=request_data["is_checked"]
    )
    return checklist_item_with_entity_dto
