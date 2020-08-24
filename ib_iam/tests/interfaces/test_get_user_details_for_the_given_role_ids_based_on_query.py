import pytest

from ib_iam.tests.common_fixtures.reset_fixture import \
    reset_sequence_role_factory


class TestGetUserDetailsForGivenRoleIdsBasedOnQuery:

    @pytest.fixture
    def user_profile_dtos(self):
        user_ids = ["user1", "user2", "user3"]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory.create(user_id=user_id)
            for user_id in user_ids]
        return user_profile_dtos

    @pytest.fixture
    def set_up(self):
        role_ids = [
            "8738f416-b32c-4c95-99ba-48056ec10e30",
            "8738f416-b32c-4c95-99ba-48056ec10e31",
            "8738f416-b32c-4c95-99ba-48056ec10e32"]
        user_ids = ["8738f416-b32c-4c95-99ba-48056ec10e34",
                    "8738f416-b32c-4c95-99ba-48056ec10e35"]
        reset_sequence_role_factory()

        import factory
        from ib_iam.tests.factories.models import ProjectRoleFactory, \
            UserRoleFactory, UserDetailsFactory
        roles = ProjectRoleFactory.create_batch(
            size=2, id=factory.Iterator(role_ids))
        UserRoleFactory.create_batch(
            size=2, user_id=factory.Iterator(user_ids),
            role=factory.Iterator(roles))
        UserDetailsFactory.create_batch(
            size=2, user_id=factory.Iterator(user_ids),
            name=factory.Iterator(['iB', 'Hubs']))

    @pytest.mark.django_db
    def test_get_user_details_for_the_given_role_ids_based_on_query(
            self, user_profile_dtos, set_up, mocker):
        # Arrange
        role_ids = [
            "8738f416-b32c-4c95-99ba-48056ec10e30",
            "8738f416-b32c-4c95-99ba-48056ec10e31"]

        from ib_iam.adapters.dtos import SearchQueryWithPaginationDTO
        search_query_with_pagination_dto = SearchQueryWithPaginationDTO(
            offset=0, limit=1, search_query='b'
        )

        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import \
            prepare_profile_bulk_mock
        get_user_profile_mock = prepare_profile_bulk_mock(mocker)
        get_user_profile_mock.return_value = user_profile_dtos
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        result = service_interface. \
            get_user_details_for_the_given_role_ids_based_on_query(
                role_ids=role_ids,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto)

        # Assert
        assert result == user_profile_dtos
