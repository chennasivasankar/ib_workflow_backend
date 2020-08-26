from unittest.mock import Mock

import pytest


class TestAddSpecificProjectDetailsInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.add_specific_project_details_presenter_interface import \
            AddSpecificProjectDetailsPresenterInterface
        presenter = create_autospec(AddSpecificProjectDetailsPresenterInterface)
        return presenter

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.add_specific_project_details_interactor import \
            AddSpecificProjectDetailsInteractor
        interactor = AddSpecificProjectDetailsInteractor(
            user_storage=storage_mock)
        return interactor

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_user_id_with_role_ids_dtos
    ):
        # Arrange
        project_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos

        expected_presenter_prepare_success_response_for_add_specific_project_details = \
            Mock()
        presenter_mock.prepare_success_response_for_add_specific_project_details. \
            return_value = expected_presenter_prepare_success_response_for_add_specific_project_details

        # Act
        response = interactor.add_specific_project_details_wrapper(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_add_specific_project_details

        storage_mock.add_project_specific_details.assert_called_once_with(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )
        presenter_mock.prepare_success_response_for_add_specific_project_details. \
            assert_called_once()

    @pytest.fixture()
    def prepare_user_id_with_role_ids_dtos(self):
        user_id_with_role_ids_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": ["ROLE_1", "ROLE_2"]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": ["ROLE_3"]
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": []
            }
        ]
        from ib_iam.tests.factories.interactor_dtos import \
            UserIdWithRoleIdsDTOFactory
        user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTOFactory(
                user_id=user_id_with_role_ids_dict["user_id"],
                role_ids=user_id_with_role_ids_dict["role_ids"]
            )
            for user_id_with_role_ids_dict in user_id_with_role_ids_list
        ]
        return user_id_with_role_ids_dtos
