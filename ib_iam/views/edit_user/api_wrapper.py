from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from ib_iam.interactors.edit_user_interactor import EditUserInteractor
from ib_iam.presenters.edit_user_presenter_implementation import \
    EditUserPresenterImplementation
from ib_iam.storages.user_storage_implementation import \
    UserStorageImplementation
from .validator_class import ValidatorClass
from ...storages.elastic_storage_implementation import \
    ElasticStorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    storage = UserStorageImplementation()
    presenter = EditUserPresenterImplementation()
    elastic_storage = ElasticStorageImplementation()
    interactor = EditUserInteractor(
        user_storage=storage, elastic_storage=elastic_storage
    )

    admin_user_id = kwargs['user'].user_id
    user_id = kwargs["path_params"]["user_id"]
    request_object = kwargs["request_data"]
    name = request_object['name']
    email = request_object['email']
    company_id = request_object['company_id']
    team_ids = request_object['team_ids']
    # role_ids = request_object['role_ids']

    from ib_iam.interactors.dtos.dtos import \
        AddUserDetailsDTO
    add_user_details_dto = AddUserDetailsDTO(
        name=name, email=email, team_ids=team_ids,
        company_id=company_id
    )

    response = interactor.edit_user_wrapper(
        admin_user_id=admin_user_id, user_id=user_id,
        add_user_details_dto=add_user_details_dto,
        presenter=presenter)
    return response
