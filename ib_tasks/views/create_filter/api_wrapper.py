from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


def get_conditions_dtos(conditions):
    from ib_tasks.interactors.filter_dtos import CreateConditionDTO
    return [
        CreateConditionDTO(
            field_id=condition['field_id'],
            operator=condition['operator'],
            value=condition['value']
        )
        for condition in conditions
    ]


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = user.user_id
    request_data = kwargs['request_data']
    from ib_tasks.interactors.filter_dtos import CreateFilterDTO
    filter_dto = CreateFilterDTO(
        filter_name=request_data['name'],
        template_id=request_data['template_id'],
        user_id=user_id,
        project_id=request_data['project_id']
    )
    conditions = request_data['conditions']
    condition_dtos = get_conditions_dtos(conditions=conditions)
    from ib_tasks.storages.filter_storage_implementation import \
        FilterStorageImplementation
    storage = FilterStorageImplementation()
    from ib_tasks.presenters.filter_presenter_implementation import \
        FilterPresenterImplementation
    presenter = FilterPresenterImplementation()
    from ib_tasks.interactors.filters.create_or_update_or_delete_filters import CreateOrUpdateOrDeleteFiltersInteractor
    from ib_tasks.storages.fields_storage_implementation import \
        FieldsStorageImplementation
    interactor = CreateOrUpdateOrDeleteFiltersInteractor(
        filter_storage=storage,
        presenter=presenter,
        field_storage=FieldsStorageImplementation()
    )
    response = interactor.create_filter_wrapper(
        filter_dto=filter_dto,
        condition_dtos=condition_dtos
    )
    return response

