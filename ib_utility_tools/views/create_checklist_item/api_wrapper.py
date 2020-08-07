from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    checklist_item_with_entity_dto = _prepare_checklist_item_with_entity_dto(
        request_data=request_data)

    from ib_utility_tools.storages.checklist_storage_implementation import \
        ChecklistStorageImplementation
    from ib_utility_tools.presenters. \
        create_checklist_item_presenter_implementation import \
        CreateChecklistItemPresenterImplementation
    from ib_utility_tools.interactors.create_checklist_item_interactor import \
        CreateChecklistItemInteractor
    checklist_storage = ChecklistStorageImplementation()
    presenter = CreateChecklistItemPresenterImplementation()
    interactor = CreateChecklistItemInteractor(
        checklist_storage=checklist_storage)

    response_data = interactor.create_checklist_item_wrapper(
        checklist_item_with_entity_dto=checklist_item_with_entity_dto,
        presenter=presenter)
    return response_data


def _prepare_checklist_item_with_entity_dto(request_data):
    from ib_utility_tools.interactors.storage_interfaces.dtos import \
        ChecklistItemWithEntityDTO
    checklist_item_with_entity_dto = ChecklistItemWithEntityDTO(
        entity_id=request_data["entity_id"],
        entity_type=request_data["entity_type"],
        text=request_data["text"],
        is_checked=request_data["is_checked"])
    return checklist_item_with_entity_dto
