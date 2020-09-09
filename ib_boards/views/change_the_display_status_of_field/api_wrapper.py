from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs["user"]
    column_id = kwargs['column_id']
    field_id = kwargs['request_data']['field_id']
    display_status = kwargs['request_data']['display_status']
    from ib_boards.interactors.dtos import ChangeFieldsStatusParameter
    field_display_status_parameter = ChangeFieldsStatusParameter(
        user_id=user.user_id,
        field_id=field_id,
        column_id=column_id,
        display_status=display_status
    )
    from ib_boards.storages.storage_implementation import StorageImplementation
    storage = StorageImplementation()
    from ib_boards.presenters.presenter_implementation import \
        FieldsDisplayStatusPresenterImplementation
    presenter = FieldsDisplayStatusPresenterImplementation()
    from ib_boards.interactors.change_field_display_status_in_columns_list_view import \
        ChangeFieldsDisplayStatus
    interactor = ChangeFieldsDisplayStatus(
        storage=storage
    )
    interactor.change_field_display_status_wrapper(
        field_display_status_parameter=field_display_status_parameter,
        presenter=presenter
    )
