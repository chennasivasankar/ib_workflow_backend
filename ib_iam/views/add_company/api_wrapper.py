from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyWithUserIdsDTO
from ib_iam.presenters.add_company_presenter_implementation import \
    AddCompanyPresenterImplementation
from ib_iam.storages.company_storage_implementation import CompanyStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.user_id)
    request_data = kwargs["request_data"]
    name = request_data["name"]
    description = request_data["description"]
    logo_url = request_data["logo_url"]
    user_ids = request_data["employee_ids"]

    storage = CompanyStorageImplementation()
    presenter = AddCompanyPresenterImplementation()
    interactor = CompanyInteractor(storage=storage)

    company_with_user_ids_dto = CompanyWithUserIdsDTO(name=name,
                                                      logo_url=logo_url,
                                                      description=description,
                                                      user_ids=user_ids)

    response_data = interactor.add_company_wrapper(
        user_id=user_id,
        company_with_user_ids_dto=company_with_user_ids_dto,
        presenter=presenter)

    return response_data
