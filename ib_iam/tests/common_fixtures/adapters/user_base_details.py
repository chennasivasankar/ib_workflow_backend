def get_basic_user_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService."
        "get_basic_user_dtos"
        )
    from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
    UserProfileDTOFactory.reset_sequence()
    user_ids = [
        "123e4567-e89b-12d3-a456-426614174000",
        "123e4567-e89b-12d3-a456-426614174001"
    ]
    import factory
    basic_user_details_dtos = UserProfileDTOFactory.create_batch(
        size=2, user_id=factory.Iterator(user_ids)
    )
    mock.return_value = basic_user_details_dtos
    return mock
