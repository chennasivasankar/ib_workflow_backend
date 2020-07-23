from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces \
    .company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyDetailsWithUserIdsDTO
from ib_iam.presenters.add_company_presenter_implementation import \
    AddCompanyPresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    user_id = str(user_object.id)
    request_data = kwargs["request_data"]
    name = request_data["name"]
    description = request_data["description"]
    logo_url = request_data["logo_url"]
    user_ids = request_data["user_ids"]

    # TODO After implementing storage implementation change that here
    # TODO Change storage interface to implementation
    storage = CompanyStorageInterface()
    presenter = AddCompanyPresenterImplementation()
    interactor = CompanyInteractor(storage=storage)

    company_details_with_user_ids_dto = CompanyDetailsWithUserIdsDTO(
        name=name,
        logo_url=logo_url,
        description=description,
        user_ids=user_ids
    )

    response_data = interactor.add_company_wrapper(
        user_id=user_id,
        company_details_with_user_ids_dto=company_details_with_user_ids_dto,
        presenter=presenter
    )

    return response_data
