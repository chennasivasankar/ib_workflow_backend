from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.get_companies import GetCompaniesInteractor
from ib_iam.presenters.get_companies_presenter_implementation import \
    GetCompaniesPresenterImplementation
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)
    storage = CompanyStorageImplementation()
    presenter = GetCompaniesPresenterImplementation()
    interactor = GetCompaniesInteractor(storage=storage)

    response_data = interactor.get_companies_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response_data
