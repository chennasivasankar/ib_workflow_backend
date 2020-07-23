from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.presenters.delete_company_presenter_implementation import \
    DeleteCompanyPresenterImplementation
from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.id)
    company_id = kwargs["company_id"]

    # TODO change this storage interface to storage implementation after completing storages
    storage = CompanyStorageInterface()
    presenter = DeleteCompanyPresenterImplementation()
    interactor = CompanyInteractor(storage=storage)

    response = interactor.delete_company_wrapper(
        user_id=user_id,
        company_id=company_id,
        presenter=presenter
    )
    return response
