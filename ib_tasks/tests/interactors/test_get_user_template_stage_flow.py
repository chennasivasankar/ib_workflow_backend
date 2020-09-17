import pytest

from ib_tasks.tests.factories.storage_dtos import StageMinimalDTOFactory, \
    StageFlowDTOFactory
from ib_tasks.tests.interactors.super_storage_mock_class import \
    StorageMockClass


class TestGetPermittedTemplateStageFlowToUser(StorageMockClass):

    @staticmethod
    @pytest.fixture()
    def interactor(task_template_storage, stage_storage, action_storage_mock):
        from ib_tasks.interactors.get_permitted_template_stage_flow_to_user \
            import GetPermittedTemplateStageFlowToUser
        interactor = GetPermittedTemplateStageFlowToUser(
            template_storage=task_template_storage,
            stage_storage=stage_storage,
            action_storage=action_storage_mock
        )
        return interactor

    @staticmethod
    @pytest.fixture()
    def presenter():
        from ib_tasks.interactors.presenter_interfaces.get_template_stage_flow_presenter_interface import \
            GetTemplateStageFlowPresenterInterface
        from unittest.mock import create_autospec
        storage = create_autospec(GetTemplateStageFlowPresenterInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def projects_mock(mocker):
        path = "ib_tasks.adapters.auth_service.AuthService.validate_project_ids"
        return mocker.patch(path)

    def test_invalid_template_raises_exception(
            self, interactor, presenter, task_template_storage
    ):
        # Arrange
        template_id = "template_1"
        user_id = "user_1"
        project_id = "project_1"
        task_template_storage.check_is_template_exists.return_value = False

        # Act
        interactor.get_template_stage_flow_to_user_wrapper(
            template_id=template_id, project_id=project_id, user_id=user_id,
            presenter=presenter
        )

        # Assert
        dict_obj = presenter.raise_invalid_task_template_id.call_args.kwargs
        expected_template_id = dict_obj['err'].task_template_id
        assert template_id == expected_template_id

    def test_invalid_project_raises_exception(
            self, interactor, presenter, task_template_storage, projects_mock
    ):
        # Arrange
        template_id = "template_1"
        user_id = "user_1"
        project_id = "project_1"
        task_template_storage.check_is_template_exists.return_value = True
        projects_mock.return_value = []

        # Act
        interactor.get_template_stage_flow_to_user_wrapper(
            template_id=template_id, project_id=project_id,
            user_id=user_id, presenter=presenter
        )

        # Assert
        dict_obj = presenter.get_response_for_invalid_project_id.call_args.kwargs
        expected_project_ids = dict_obj['err'].invalid_project_ids
        assert project_id == expected_project_ids[0]

    @pytest.fixture()
    def user_in_projects_mock(self, mocker):
        path = "ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_project"
        return mocker.patch(path)

    def test_user_not_in_project_raises_exception(
            self, interactor, presenter, task_template_storage,
            projects_mock, user_in_projects_mock
    ):
        # Arrange
        template_id = "template_1"
        user_id = "user_1"
        project_id = "project_1"
        task_template_storage.check_is_template_exists.return_value = True
        projects_mock.return_value = [project_id]
        user_in_projects_mock.return_value = False

        # Act
        interactor.get_template_stage_flow_to_user_wrapper(
            template_id=template_id, project_id=project_id,
            user_id=user_id, presenter=presenter
        )

        # Assert
        presenter.get_response_for_user_not_in_project.assert_called_once()

    @pytest.fixture()
    def set_up_storage(self, task_template_storage,
                       projects_mock, user_in_projects_mock,
                       stage_storage, action_storage_mock,
                       ):
        project_id = "project_1"
        action_ids = [1]
        task_template_storage.check_is_template_exists.return_value = True
        projects_mock.return_value = [project_id]
        user_in_projects_mock.return_value = True
        stage_dtos = StageMinimalDTOFactory.create_batch(1)
        stage_flow_dtos = StageFlowDTOFactory.create_batch(1)
        stage_storage.get_stages_in_template.return_value = stage_dtos
        action_storage_mock.get_action_ids_given_stage_ids.return_value = action_ids
        stage_storage.get_stage_flows_to_user.return_value = stage_flow_dtos

    @classmethod
    def setup(cls):
        StageMinimalDTOFactory.reset_sequence(1)
        StageFlowDTOFactory.reset_sequence(1)

    def expected_response(self):
        self.setup()
        from ib_tasks.tests.factories.presenter_dtos \
            import StageFlowCompleteDetailsDTOFactory
        return StageFlowCompleteDetailsDTOFactory()

    def test_given_valid_details_returns_details(
            self, interactor, presenter, task_template_storage,
            projects_mock, user_in_projects_mock, set_up_storage,
            stage_storage, action_storage_mock
    ):
        # Arrange
        template_id = "template_1"
        user_id = "user_1"
        project_id = "project_1"
        action_ids = [1]
        stage_ids = [1]
        stage_flow_complete_details = self.expected_response()

        # Act
        interactor.get_template_stage_flow_to_user_wrapper(
            template_id=template_id, project_id=project_id,
            user_id=user_id, presenter=presenter
        )

        # Assert
        stage_storage.get_stages_in_template.assert_called_once_with(
            template_id=template_id
        )
        action_storage_mock.get_action_ids_given_stage_ids.assert_called_once_with(
            stage_ids=stage_ids
        )
        stage_storage.get_stage_flows_to_user.assert_called_once_with(
            stage_ids=stage_ids, action_ids=action_ids
        )
        presenter.get_response_for_template_stage_flow.assert_called_once_with(
            stage_flow_complete_details_dto=stage_flow_complete_details
        )
