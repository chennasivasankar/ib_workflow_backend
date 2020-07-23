from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.get_companies import GetCompaniesInteractor
from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface
from ib_iam.presenters.get_companies_presenter_implementation import \
    GetCompaniesPresenterImplementation


# TODO After writing Company storages implement the storage in api wrapper(get_companies)

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.id)
    storage = CompanyStorageInterface()
    presenter = GetCompaniesPresenterImplementation()
    interactor = GetCompaniesInteractor(storage=storage)

    response_data = interactor.get_companies_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response_data
