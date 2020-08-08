from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.get_companies_interactor import GetCompaniesInteractor
from ib_iam.presenters.get_companies_presenter_implementation import \
    GetCompaniesPresenterImplementation
from ib_iam.storages.company_storage_implementation import \
    CompanyStorageImplementation
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)
    company_storage = CompanyStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = GetCompaniesPresenterImplementation()
    interactor = GetCompaniesInteractor(company_storage=company_storage,
                                        user_storage=user_storage)

    response_data = interactor.get_companies_wrapper(
        user_id=user_id, presenter=presenter
    )
    return response_data
