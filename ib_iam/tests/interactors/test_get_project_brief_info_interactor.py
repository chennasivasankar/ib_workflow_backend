from unittest.mock import create_autospec, Mock

import pytest


class TestGetProjectBriefInfoInteractor:

    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        project_storage = create_autospec(ProjectStorageInterface)
        return project_storage

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface \
            import UserStorageInterface
        project_storage = create_autospec(UserStorageInterface)
        return project_storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.get_project_brief_info_presenter_interface import \
            GetProjectBriefInfoPresenterInterface
        presenter = create_autospec(GetProjectBriefInfoPresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, project_storage, user_storage):
        from ib_iam.interactors.get_project_brief_info_interactor import \
            GetProjectBriefInfoInteractor
        interactor = GetProjectBriefInfoInteractor(
            project_storage=project_storage, user_storage=user_storage
        )
        return interactor

    # @pytest.fixture()
    # def pagination_dto(self):
    #     from ib_iam.tests.factories.storage_dtos import PaginationDTOFactory
    #
    #     limit = 5
    #     offset = 0
    #     pagination_dto = PaginationDTOFactory(
    #         limit=limit,
    #         offset=offset
    #     )
    #     return pagination_dto

    # def test_with_invalid_limit_value_return_response(
    #         self, interactor, project_storage, presenter, pagination_dto
    # ):
    #     # Arrange
    #     user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
    #     limit = -1
    #     pagination_dto.limit = limit
    #
    #     expected_presenter_response_for_invalid_limit_mock = Mock()
    #
    #     presenter.response_for_invalid_limit.return_value = \
    #         expected_presenter_response_for_invalid_limit_mock
    #
    #     # Act
    #     response = interactor.get_project_brief_info_wrapper(
    #         pagination_dto=pagination_dto, user_id=user_id,
    #         presenter=presenter
    #     )
    #
    #     # Assert
    #     assert response == expected_presenter_response_for_invalid_limit_mock
    #
    #     presenter.response_for_invalid_limit.assert_called_once()
    #
    # def test_with_invalid_offset_value_return_response(
    #         self, interactor, project_storage, presenter, pagination_dto
    # ):
    #     # Arrange
    #     user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
    #     offset = -1
    #     pagination_dto.offset = offset
    #
    #     expected_presenter_response_for_invalid_offset_mock = Mock()
    #
    #     presenter.response_for_invalid_offset.return_value = \
    #         expected_presenter_response_for_invalid_offset_mock
    #
    #     # Act
    #     response = interactor.get_project_brief_info_wrapper(
    #         pagination_dto=pagination_dto, user_id=user_id,
    #         presenter=presenter
    #     )
    #
    #     # Assert
    #     assert response == expected_presenter_response_for_invalid_offset_mock
    #
    #     presenter.response_for_invalid_offset.assert_called_once()

    @pytest.fixture()
    def project_dtos(self):
        from ib_iam.tests.factories.storage_dtos import \
            ProjectWithDisplayIdDTOFactory
        ProjectWithDisplayIdDTOFactory.reset_sequence(1)

        project_ids = ["project_1", "project_2"]
        project_dtos = [
            ProjectWithDisplayIdDTOFactory(project_id=project_id)
            for project_id in project_ids
        ]
        return project_dtos

    def test_with_invalid_user_return_response(
            self, interactor, project_storage, user_storage, presenter
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_user_does_not_exist_mock = Mock()

        presenter.response_for_user_does_not_exist.return_value = \
            expected_presenter_response_for_user_does_not_exist_mock

        user_storage.is_user_exist.return_value = False

        # Act
        response = interactor.get_project_brief_info_wrapper(
            user_id=user_id, presenter=presenter
        )

        # Assert
        assert response == \
               expected_presenter_response_for_user_does_not_exist_mock

        presenter.response_for_user_does_not_exist.assert_called_once()
        user_storage.is_user_exist.assert_called_with(user_id=user_id)

    def test_with_valid_details_return_response(
            self, interactor, project_storage, user_storage, presenter,
            project_dtos
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_success_response_for_get_project_brief_info_mock = \
            Mock()

        presenter.success_response_for_get_project_brief_info.return_value = \
            expected_presenter_success_response_for_get_project_brief_info_mock

        user_storage.is_user_exist.return_value = True
        project_storage.get_user_project_dtos.return_value = project_dtos

        # Act
        response = interactor.get_project_brief_info_wrapper(
            user_id=user_id, presenter=presenter
        )

        # Assert
        assert response == \
               expected_presenter_success_response_for_get_project_brief_info_mock

        project_storage.get_user_project_dtos.assert_called_with(
            user_id=user_id
        )
        presenter.success_response_for_get_project_brief_info. \
            assert_called_once_with(project_dtos=project_dtos)
