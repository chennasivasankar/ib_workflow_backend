from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    request_data = kwargs["request_data"]
    checklist_item_ids = request_data["checklist_item_ids"]

    from ib_utility_tools.presenters \
        .delete_checklist_items_presenter_implementation import \
        DeleteChecklistItemsPresenterImplementation
    from ib_utility_tools.storages.checklist_storage_implementation import \
        ChecklistStorageImplementation
    from ib_utility_tools.interactors.delete_checklist_items_interactor \
        import DeleteChecklistItemsInteractor
    presenter = DeleteChecklistItemsPresenterImplementation()
    checklist_storage = ChecklistStorageImplementation()
    interactor = DeleteChecklistItemsInteractor(
        checklist_storage=checklist_storage)

    response = interactor.delete_checklist_items_wrapper(
        checklist_item_ids=checklist_item_ids, presenter=presenter)
    return response
