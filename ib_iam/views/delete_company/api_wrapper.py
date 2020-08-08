from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.presenters.delete_company_presenter_implementation import \
    DeleteCompanyPresenterImplementation
from ib_iam.storages.company_storage_implementation import CompanyStorageImplementation
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    company_id = kwargs["company_id"]

    company_storage = CompanyStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = DeleteCompanyPresenterImplementation()
    interactor = CompanyInteractor(company_storage=company_storage,
                                   user_storage=user_storage)

    response = interactor.delete_company_wrapper(
        user_id=user_id,
        company_id=company_id,
        presenter=presenter
    )
    return response
