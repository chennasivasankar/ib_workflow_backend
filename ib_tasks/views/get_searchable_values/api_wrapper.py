from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.field_dtos import SearchableFieldTypeDTO
from ...interactors.searchable_field_values_interactor import \
    SearchableFieldValuesInteractor
from ...presenters.searchable_field_values_presenter_implementation import \
    SearchableFieldValuesPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    params = kwargs['query_params']
    searchable_type = params['search_type']
    search_query = params['search_query']
    offset = params['offset']
    limit = params['limit']

    searchable_field_type_dto = SearchableFieldTypeDTO(
        searchable_type=searchable_type,
        offset=offset,
        limit=limit,
        search_query=search_query
    )
    presenter = SearchableFieldValuesPresenterImplementation()

    interactor = SearchableFieldValuesInteractor()
    response = interactor. \
        searchable_field_values_wrapper(presenter=presenter,
                                        searchable_field_type_dto=
                                        searchable_field_type_dto)
    return response
