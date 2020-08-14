from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_object = kwargs["user"]
    request_data = kwargs["request_data"]
    user_id_name_email_and_profile_pic_url_dto = \
        _prepare_user_id_name_email_and_profile_pic_url_dto(
            request_data=request_data, user_object=user_object)
    role_ids = request_data.get("role_ids", [])

    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    from ib_iam.presenters \
        .update_user_profile_presenter_implementation import \
        UpdateUserProfilePresenterImplementation
    presenter = UpdateUserProfilePresenterImplementation()
    from ib_iam.interactors.update_user_profile_interactor import \
        UpdateUserProfileInteractor
    interactor = UpdateUserProfileInteractor(user_storage=user_storage)

    response_data = interactor.update_user_profile_wrapper(
        user_profile_dto=user_id_name_email_and_profile_pic_url_dto,
        role_ids=role_ids,
        presenter=presenter)
    return response_data


def _prepare_user_id_name_email_and_profile_pic_url_dto(request_data,
                                                        user_object):
    from ib_iam.interactors.storage_interfaces.dtos import \
        UserProfileDTO
    user_id_name_email_and_profile_pic_url_dto = \
        UserProfileDTO(
            user_id=user_object.user_id,
            name=request_data["name"],
            email=request_data["email"],
            profile_pic_url=request_data["profile_pic_url"]
        )
    return user_id_name_email_and_profile_pic_url_dto
