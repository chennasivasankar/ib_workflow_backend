from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    add_or_edit_group_by_parameter_dto = prepare_add_or_edit_group_by_parameter_dto(
        kwargs
    )

    from ib_adhoc_tasks.interactors.group_by_interactor import \
        GroupByInteractor
    from ib_adhoc_tasks.storages.storage_implementation import \
        StorageImplementation
    storage = StorageImplementation()
    from ib_adhoc_tasks.presenters.add_or_edit_group_by_presenter_implementation import \
        AddOrEditGroupByPresenterImplementation
    presenter = AddOrEditGroupByPresenterImplementation()
    interactor = GroupByInteractor(storage=storage)

    return interactor.add_or_edit_group_by_wrapper(
        add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto,
        presenter=presenter
    )


def prepare_add_or_edit_group_by_parameter_dto(kwargs):
    user_object = kwargs["user"]
    request_data = kwargs["request_data"]
    from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
        AddOrEditGroupByParameterDTO
    return AddOrEditGroupByParameterDTO(
        user_id=str(user_object.user_id),
        project_id=kwargs["query_params"]["project_id"],
        view_type=request_data["view_type"],
        group_by_key=request_data["group_by_key"],
        group_by_id=request_data.get("group_by_id", None),
        order=request_data.get("order", None)
    )
