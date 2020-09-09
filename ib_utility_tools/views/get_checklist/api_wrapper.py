from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_utility_tools.interactors.storage_interfaces.dtos import EntityDTO
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    entity_dto = prepare_entity_dto(request_data=request_data)

    from ib_utility_tools.storages.checklist_storage_implementation import \
        ChecklistStorageImplementation
    from ib_utility_tools.presenters. \
        get_checklist_presenter_implementation import \
        GetChecklistPresenterImplementation
    from ib_utility_tools.interactors.get_checklist_interactor import \
        GetChecklistInteractor
    checklist_storage = ChecklistStorageImplementation()
    presenter = GetChecklistPresenterImplementation()
    interactor = GetChecklistInteractor(checklist_storage=checklist_storage)

    response_data = interactor.get_checklist_wrapper(entity_dto=entity_dto,
                                                     presenter=presenter)
    return response_data


def prepare_entity_dto(request_data) -> EntityDTO:
    entity_dto = EntityDTO(
        entity_id=request_data["entity_id"],
        entity_type=request_data["entity_type"]
    )
    return entity_dto
