from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces.dtos import CompanyWithCompanyIdAndUserIdsDTO
from ib_iam.presenters.update_company_presenter_implementation import \
    UpdateCompanyPresenterImplementation
from ib_iam.storages.company_storage_implementation import CompanyStorageImplementation
from ...storages.user_storage_implementation import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_obj = kwargs["user"]
    user_id = str(user_obj.user_id)
    request_data = kwargs["request_data"]
    company_id = kwargs["company_id"]
    name = request_data["name"]
    description = request_data["description"]
    logo_url = request_data["logo_url"]
    user_ids = request_data["employee_ids"]

    company_storage = CompanyStorageImplementation()
    user_storage = UserStorageImplementation()
    presenter = UpdateCompanyPresenterImplementation()
    interactor = CompanyInteractor(company_storage=company_storage,
                                   user_storage=user_storage)

    company_with_company_id_and_user_ids_dto = \
        CompanyWithCompanyIdAndUserIdsDTO(company_id=company_id,
                                          name=name,
                                          description=description,
                                          logo_url=logo_url,
                                          user_ids=user_ids)
    response = interactor.update_company_details_wrapper(
        user_id=user_id,
        company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
        presenter=presenter)
    return response
