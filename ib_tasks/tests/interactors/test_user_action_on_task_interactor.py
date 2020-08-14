from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.interactors.user_action_on_task_interactor \
    import UserActionOnTaskInteractor
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_task_gof_and_fields_dto, \
    prepare_call_action_logic_update_stages_mock
from ib_tasks.tests.factories.interactor_dtos import \
    TaskCurrentStageDetailsDTOFactory


class TestUserActionOnTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskCurrentStageDetailsDTOFactory.reset_sequence()

    @staticmethod
    @pytest.fixture()
    def storage():
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def gof_storage():
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def field_storage():
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import FieldsStorageInterface
        storage = create_autospec(FieldsStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def stage_storage():
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import StageStorageInterface
        storage = create_autospec(StageStorageInterface)
        return storage

    @pytest.fixture
    def elasticsearch_storage(self):
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticSearchStorageInterface
        return create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def task_stage_storage(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @staticmethod
    @pytest.fixture()
    def presenter():
        from unittest.mock import create_autospec
        from ib_tasks.interactors.presenter_interfaces.presenter_interface \
            import PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @staticmethod
    def gof_and_fields_mock(mocker, task_dto):
        path = 'ib_tasks.interactors.get_task_base_interactor' \
               '.GetTaskBaseInteractor.get_task'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_dto
        return mock_obj

    @staticmethod
    @pytest.fixture()
    def board_mock(mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture
    def task_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return create_autospec(ActionStorageInterface)

    @pytest.fixture
    def elasticsearch_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticSearchStorageInterface
        return create_autospec(ElasticSearchStorageInterface)

    @staticmethod
    def task_boards_mock(mocker, task_board_details):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_board_details
        return mock_obj

    @staticmethod
    def actions_dto_mock(mocker, actions_dto):
        path = 'ib_tasks.interactors.get_user_permitted_stage_actions' \
               '.GetUserPermittedStageActions' \
               '.get_user_permitted_stage_actions'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = actions_dto
        return mock_obj

    @pytest.fixture
    def get_task_current_stages_mock(self, mocker):
        path = "ib_tasks.interactors.get_task_current_stages_interactor" \
               ".GetTaskCurrentStagesInteractor" \
               ".get_task_current_stages_details"
        return mocker.patch(path)

    @staticmethod
    def fields_mock(mocker, fields_dto):
        path = 'ib_tasks.interactors.get_field_details.GetFieldsDetails' \
               '.get_fields_details'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = fields_dto
        return mock_obj

    @pytest.fixture
    def assignees(self):
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import \
            TaskStageAssigneeDetailsDTO
        from ib_tasks.adapters.dtos import AssigneeDetailsDTO
        return TaskStageAssigneeDetailsDTO(
            task_id=1,
            stage_id='stage_id_1',
            assignee_details=AssigneeDetailsDTO(assignee_id='1', name='name',
                                                profile_pic_url='pavan.com')
        )

    @staticmethod
    def prepare_task_complete_details(task_id, assignees,
                                      task_boards_details):
        from ib_tasks.interactors.presenter_interfaces.dtos \
            import TaskCompleteDetailsDTO
        from ib_tasks.tests.factories.storage_dtos \
            import ActionDTOFactory
        ActionDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos \
            import FieldDisplayDTOFactory
        FieldDisplayDTOFactory.reset_sequence()
        from ib_tasks.interactors.stage_dtos import TaskStageDTO
        return TaskCompleteDetailsDTO(
            task_id=task_id,
            task_boards_details=task_boards_details,
            actions_dto=[ActionDTOFactory()],
            field_dtos=[FieldDisplayDTOFactory()],
            assignees_details=[assignees],
            task_stage_details=[TaskStageDTO(stage_id='stage_1', db_stage_id=1,
                                             display_name='display_name',
                                             stage_colour='blue')]
        )

    def test_invalid_task_display_id_raises_exception(
            self, storage, presenter, gof_storage, field_storage,
            elasticsearch_storage, task_stage_storage,
            stage_storage, task_storage_mock, action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        action_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = False
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )
        mock_object = Mock()
        presenter.raise_invalid_task_display_id.return_value = mock_object

        # Act
        response = interactor.user_action_on_task_wrapper(
            presenter=presenter, task_display_id=task_display_id)

        # Assert
        assert response == mock_object
        error_obj = presenter.raise_invalid_task_display_id.call_args[0][0]
        invalid_task_display_id = error_obj.task_display_id
        assert invalid_task_display_id == task_display_id

    def test_invalid_task_raises_exception(
            self, storage, presenter, gof_storage, field_storage,
            elasticsearch_storage, task_stage_storage,
            stage_storage, task_storage_mock, action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        action_id = 1
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        storage.validate_task_id.return_value = False
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        dict_obj = presenter.raise_exception_for_invalid_task.call_args.kwargs
        expected_task_id = dict_obj['error_obj'].task_id
        assert expected_task_id == task_id

    def test_invalid_board_raises_exception(
            self, mocker, storage, presenter, gof_storage,
            field_storage, stage_storage, task_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            elasticsearch_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        action_id = 1
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = False
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage_mock,
            task_stage_storage=task_stage_storage_mock

        )

        storage.validate_task_id.return_value = True

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        dict_obj = presenter.raise_exception_for_invalid_board.call_args.kwargs
        expected_board_id = dict_obj['error_obj'].board_id
        assert board_id == expected_board_id

    def test_invalid_action_raises_exception(
            self, mocker, storage, presenter, elasticsearch_storage,
            task_stage_storage,
            gof_storage, field_storage, stage_storage, task_storage_mock,
            action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        task_id = 1
        action_id = 1
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )
        storage.validate_action.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        storage.validate_action.assert_called_once_with(action_id=action_id)
        dict_obj = \
            presenter.raise_exception_for_invalid_action.call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_invalid_present_stage_action_raises_exception(
            self, mocker, storage, presenter, elasticsearch_storage,
            task_stage_storage,
            gof_storage, field_storage, stage_storage, task_storage_mock,
            action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        action_id = 1
        action_ids = [2, 3, 4]
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        mock_obj.return_value = True

        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )
        storage.validate_action.return_value = True
        storage.get_task_present_stage_actions.return_value = action_ids

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        storage.validate_action.assert_called_once_with(action_id=action_id)
        dict_obj = presenter.raise_exception_for_invalid_present_actions \
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    def test_given_user_permission_denied_raises_exception(
            self, mocker, storage, presenter, elasticsearch_storage,
            task_stage_storage,
            gof_storage, field_storage, stage_storage, task_storage_mock,
            action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        task_id = 1
        action_id = 1
        action_ids = [1, 3, 4]
        storage.get_task_present_stage_actions.return_value = action_ids
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        user_roles_mock = mocker.patch(
            'ib_tasks.adapters.roles_service.RolesService.get_user_roles')
        user_roles_mock.return_value = ["ROLE_1", "ROLE_3"]
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        path = 'ib_tasks.interactors.user_role_validation_interactor' \
               '.UserRoleValidationInteractor' \
               '.does_user_has_required_permission'
        validation_mock_obj = mocker.patch(path)
        validation_mock_obj.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        user_roles_mock.called_once()
        dict_obj = \
            presenter.raise_exception_for_user_action_permission_denied \
                .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id
        validation_mock_obj.called_once()

    def test_given_user_board_permission_denied_raises_exception(
            self, mocker, storage, presenter, elasticsearch_storage,
            task_stage_storage,
            gof_storage, field_storage, stage_storage, board_mock,
            task_storage_mock, action_storage_mock):
        # Arrange
        user_id = "user_1"
        board_id = "board_1"
        task_display_id = "task_1"
        task_id = 1
        action_id = 1
        action_ids = [1, 3, 4]
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        storage.get_task_present_stage_actions.return_value = action_ids
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage
        )
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_task_gof_and_fields_dto
        task_dto = prepare_task_gof_and_fields_dto()
        gof_and_fields_mock = self.gof_and_fields_mock(mocker, task_dto)
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_call_action_logic_update_stages_mock
        call_action_mock = prepare_call_action_logic_update_stages_mock(mocker)
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        path = 'ib_tasks.interactors.user_role_validation_interactor' \
               '.UserRoleValidationInteractor' \
               '.does_user_has_required_permission'
        validation_mock_obj = mocker.patch(path)
        validation_mock_obj.return_value = True
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_stage_display_satisfied_stage_ids
        stage_mock = prepare_stage_display_satisfied_stage_ids(mocker)
        stage_ids = ['stage_1', 'stage_2']
        stage_mock.return_value = stage_ids

        from ib_tasks.exceptions.permission_custom_exceptions \
            import UserBoardPermissionDenied
        board_mock.side_effect = UserBoardPermissionDenied(board_id=board_id)

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        gof_and_fields_mock.called_once()
        call_action_mock.called_once()
        dict_obj = presenter.raise_exception_for_user_board_permission_denied \
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].board_id
        assert board_id == expected_action_id
        storage.update_task_stages \
            .assert_called_once_with(stage_ids=stage_ids, task_id=task_id)
        validation_mock_obj.called_once()

    def test_given_valid_details_returns_task_complete_details(
            self, mocker, storage, presenter, elasticsearch_storage,
            task_stage_storage, assignees,
            gof_storage, field_storage, stage_storage, board_mock,
            task_storage_mock, action_storage_mock,
            get_task_current_stages_mock):
        # Arrange
        user_id = "1"
        board_id = "board_1"
        task_display_id = "task_1"
        task_id = 1
        action_id = 1
        action_ids = [1, 3, 4]
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        storage.get_task_present_stage_actions.return_value = action_ids
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService.validate_board_id')
        mock_obj.return_value = True
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        get_task_current_stages_mock.return_value = \
            task_current_stages_details
        storage.validate_task_id.return_value = True
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage

        )
        task_dto = prepare_task_gof_and_fields_dto()
        gof_and_fields_mock = self.gof_and_fields_mock(mocker, task_dto)
        call_action_mock = prepare_call_action_logic_update_stages_mock(mocker)
        storage.validate_action.return_value = True
        storage.get_action_roles.return_value = ["ROLE_2", "ROLE_4"]
        path = 'ib_tasks.interactors.user_role_validation_interactor' \
               '.UserRoleValidationInteractor' \
               '.does_user_has_required_permission'
        validation_mock_obj = mocker.patch(path)
        validation_mock_obj.return_value = True
        from ib_tasks.tests.common_fixtures.interactors import (

            prepare_stage_display_satisfied_stage_ids,
            prepare_task_boards_details, prepare_fields_and_actions_dto,
            prepare_mock_for_next_stage_random_assignees,
            prepare_assignees_interactor_mock
        )
        prepare_assignees_interactor_mock(mocker, assignees)
        prepare_mock_for_next_stage_random_assignees(mocker)
        task_board_details = prepare_task_boards_details()
        stage_mock = prepare_stage_display_satisfied_stage_ids(mocker)
        task_stage_details_dto = prepare_fields_and_actions_dto(mocker)
        task_complete_details = self.prepare_task_complete_details(
            task_id=task_id, task_boards_details=task_board_details,
            assignees=assignees
        )
        stage_ids = ['stage_1', 'stage_2']
        stage_mock.return_value = stage_ids
        board_mock.return_value = task_board_details

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        mock_obj.called_once()
        gof_and_fields_mock.called_once()
        call_action_mock.called_once()
        board_mock.called_once()
        storage.update_task_stages \
            .assert_called_once_with(stage_ids=stage_ids, task_id=task_id)
        task_stage_details_dto.called_once()
        validation_mock_obj.called_once()
        presenter.get_response_for_user_action_on_task \
            .assert_called_once_with(
            task_complete_details_dto=task_complete_details,
            task_current_stage_details_dto=task_current_stages_details
        )
