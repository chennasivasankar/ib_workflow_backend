from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs["user"]
    column_id = kwargs['column_id']
    field_id = kwargs['field_id']
    display_order = kwargs['request_data']['display_order']
    field_ids = kwargs['request_data']['display_order']
    from ib_boards.interactors.dtos import ChangeFieldsOrderParameter
    field_order_parameter = ChangeFieldsOrderParameter(
        user_id=user.user_id,
        field_id=field_id,
        column_id=column_id,
        display_order=display_order,
        field_ids=field_ids
    )
    from ib_boards.storages.storage_implementation import StorageImplementation
    storage = StorageImplementation()
    from ib_boards.presenters.presenter_implementation import \
        FieldsDisplayOrderPresenterImplementation
    presenter = FieldsDisplayOrderPresenterImplementation()

    from ib_boards.interactors.change_field_order_in_column_list_view import \
        ChangeFieldsDisplayOrder
    interactor = ChangeFieldsDisplayOrder(
        storage=storage
    )
    interactor.change_field_display_order_wrapper(
        field_order_parameter=field_order_parameter,
        presenter=presenter
    )
