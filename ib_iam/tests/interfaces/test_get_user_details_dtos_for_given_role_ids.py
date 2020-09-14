import pytest

from ib_iam.tests.common_fixtures.reset_fixture import \
    reset_sequence_role_factory, reset_sequence_company_factory, \
    reset_sequence_user_details_factory
from ib_iam.tests.factories.models import CompanyFactory, UserDetailsFactory, \
    ProjectFactory


class TestGetUserDetailsBulkForGivenRoleIds:

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
        role_ids = ["12233442", "12312323", "4141264557"]
        user_ids = ["user1", "user2", "user3"]
        project_id = "FA"
        user_roles = [
            {"role_id": role_id, "user_id": user_ids[index]}
            for index, role_id in enumerate(role_ids)
        ]
        reset_sequence_role_factory()
        from ib_iam.tests.factories.models import UserRoleFactory, \
            ProjectRoleFactory
        ProjectFactory.reset_sequence(0)
        project_object = ProjectFactory.create(project_id=project_id)
        for user_role in user_roles:
            role_object = ProjectRoleFactory.create(
                role_id=user_role["role_id"],
                project=project_object
            )
            UserRoleFactory.create(
                project_role=role_object, user_id=user_role["user_id"])
        return role_ids

    @pytest.mark.django_db
    def test_get_user_details_dtos_for_given_valid_role_ids(
            self, user_profile_dtos, set_up, mocker
    ):
        # Arrange
        role_ids = set_up
        project_id = "FA"
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_basic_user_profile_dtos_mock
        get_user_profile_mock = get_basic_user_profile_dtos_mock(mocker)
        get_user_profile_mock.return_value = user_profile_dtos
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        expected_result = service_interface.get_user_details_for_given_role_ids(
            role_ids=role_ids, project_id=project_id
        )

        # Assert
        assert len(expected_result) == len(user_profile_dtos)
        self._check_are_valid_user_dtos(
            expected_result=expected_result, actual_result=user_profile_dtos
        )

    @pytest.mark.django_db
    def test_given_invalid_role_ids_then_raise_exception(self):
        # Arrange
        invalid_role_ids = ["1", "2", "3"]
        project_id = "FA"
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import \
            InvalidRoleIdsForProject
        with pytest.raises(InvalidRoleIdsForProject):
            service_interface.get_user_details_for_given_role_ids(
                role_ids=invalid_role_ids, project_id=project_id
            )

    @pytest.mark.django_db
    def test_given_valid_role_ids_with_all_role_id_then_return_all_users(
            self, mocker
    ):
        # Arrange
        role_ids = ["ALL_ROLES", "1", "2"]
        users = [
            {
                "user_id": "3",
                "is_admin": True
            },
            {
                "user_id": "4",
                "is_admin": False
            },
            {
                "user_id": "5",
                "is_admin": False
            },
            {
                "user_id": "6",
                "is_admin": False
            }
        ]
        project_id = "FA"
        actual_user_ids = ["4", "5", "6"]
        reset_sequence_company_factory()
        reset_sequence_user_details_factory()
        for user in users:
            company = CompanyFactory.create()
            UserDetailsFactory.create(
                user_id=user["user_id"], is_admin=user["is_admin"],
                company=company)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory.create(user_id=user_id)
            for user_id in actual_user_ids]
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            get_basic_user_profile_dtos_mock
        get_user_profile_mock = get_basic_user_profile_dtos_mock(mocker)
        get_user_profile_mock.return_value = user_profile_dtos
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        expected_result = service_interface.get_user_details_for_given_role_ids(
            role_ids=role_ids, project_id=project_id
        )

        # Assert
        assert len(expected_result) == len(user_profile_dtos)
        self._check_are_valid_user_dtos(
            expected_result=expected_result, actual_result=user_profile_dtos)

    @staticmethod
    def _check_are_valid_user_dtos(expected_result, actual_result):
        for index, user_details_dto in enumerate(actual_result):
            assert expected_result[index].user_id == user_details_dto.user_id
            assert expected_result[index].name == user_details_dto.name
            assert expected_result[index].profile_pic_url == \
                   user_details_dto.profile_pic_url
