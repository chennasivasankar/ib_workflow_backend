from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor
from ib_iam.presenters.add_new_user_presenter_implementation \
    import AddUserPresenterImplementation
from ib_iam.storages.user_storage_implementation \
    import UserStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = AddUserPresenterImplementation()
    interactor = AddNewUserInteractor(user_storage=storage)

    user = kwargs['user']
    user_id = user.user_id
    request_object = kwargs["request_data"]
    name = request_object['name']
    email = request_object['email']
    company_id = request_object['company_id']
    team_ids = request_object['team_ids']
    role_ids = request_object['role_ids']

    from ib_iam.interactors.DTOs.common_dtos import \
        UserDetailsWithTeamRoleAndCompanyIdsDTO
    user_details_with_team_role_and_company_ids_dto \
        = UserDetailsWithTeamRoleAndCompanyIdsDTO(
        name=name, email=email, team_ids=team_ids, role_ids=role_ids,
        company_id=company_id
    )

    response = interactor.add_new_user_wrapper(
        user_id=user_id,
        user_details_with_team_role_and_company_ids_dto\
            = user_details_with_team_role_and_company_ids_dto,
        presenter=presenter
    )

    return response
