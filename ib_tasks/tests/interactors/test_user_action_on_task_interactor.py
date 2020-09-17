import datetime
from unittest.mock import create_autospec

import pytest

from ib_tasks.constants.enum import ActionTypes, ViewType
from ib_tasks.interactors.user_action_on_task.user_action_on_task_interactor \
    import UserActionOnTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    TaskCurrentStageDetailsDTOFactory, FieldDisplayDTOFactory
from ib_tasks.tests.factories.storage_dtos import (
    ActionDTOFactory, StageActionDetailsDTOFactory,
    TaskDetailsDTOFactory,
    TaskGoFDTOFactory, TaskGoFFieldDTOFactory,
    GoFIdWithGoFDisplayNameDTOFactory, FieldIdWithFieldDisplayNameDTOFactory
)
from ib_tasks.tests.interactors.super_storage_mock_class import \
    StorageMockClass


class TestUserActionOnTaskInteractor(StorageMockClass):

    @classmethod
    def set_up(cls):
        ActionDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        TaskCurrentStageDetailsDTOFactory.reset_sequence()
        TaskCurrentStageDetailsDTOFactory.reset_sequence()
        ActionDTOFactory.reset_sequence()
        FieldDisplayDTOFactory.reset_sequence()
        TaskGoFDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()

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

    @pytest.fixture()
    def user_project_roles_mock(self, mocker):
        path = "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids_based_on_project"
        return mocker.patch(path)

    @staticmethod
    @pytest.fixture()
    def board_mock(mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'
        mock_obj = mocker.patch(path)
        return mock_obj

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
        from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
        from ib_tasks.adapters.dtos import AssigneeDetailsDTO
        return TaskStageAssigneeDetailsDTO(
                task_id=1,
                stage_id='stage_id_1',
                assignee_details=AssigneeDetailsDTO(assignee_id='1',
                                                    name='name',
                                                    profile_pic_url='pavan.com')
        )

    @staticmethod
    def prepare_task_complete_details(task_id, assignees,
                                      task_display_id):
        from ib_tasks.interactors.presenter_interfaces.dtos \
            import TaskCompleteDetailsDTO
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_task_boards_details
        task_board_details = prepare_task_boards_details()
        from ib_tasks.interactors.stage_dtos import TaskStageDTO
        return TaskCompleteDetailsDTO(
                task_id=task_id,
                task_display_id=task_display_id,
                task_boards_details=task_board_details,
                actions_dto=[ActionDTOFactory()],
                field_dtos=[FieldDisplayDTOFactory()],
                assignees_details=[assignees],
                task_stage_details=[
                    TaskStageDTO(
                        stage_id='stage_1', db_stage_id=1,
                        display_name='display_name',
                        stage_colour='blue')
                ]
        )

    @pytest.fixture()
    def random_assignee_mock(self, mocker):
        path = 'ib_tasks.interactors.get_and_update_assignees_having_less_tasks_counts_for_next_stages_interactor' \
               '.GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor' \
               '.get_random_assignees_of_next_stages_and_update_in_db'
        return mocker.patch(path)

    @pytest.fixture()
    def user_in_project_mock(self, mocker):
        path = 'ib_tasks.adapters.auth_service.AuthService' \
               '.validate_if_user_is_in_project'
        return mocker.patch(path)

    @pytest.fixture()
    def filtered_task_overview_user(self, mocker):
        path = \
            'ib_tasks.interactors' \
            '.get_all_task_overview_with_filters_and_searches_for_user' \
            '.GetTasksOverviewForUserInteractor' \
            '.get_filtered_tasks_overview_for_user'
        return mocker.patch(path)

    @pytest.fixture()
    def task_template_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
            import TaskTemplateStorageInterface
        return create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture()
    def create_task_storage(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        return create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture()
    def interactor(
            self, storage, presenter, gof_storage, field_storage,
            elasticsearch_storage, task_stage_storage,
            stage_storage, task_storage_mock, action_storage_mock,
            user_in_project_mock, task_template_storage,
            create_task_storage
    ):
        user_id = "user_1"
        board_id = "board_1"
        action_id = 1
        interactor = UserActionOnTaskInteractor(
            user_id=user_id, board_id=board_id, action_id=action_id,
            storage=storage, gof_storage=gof_storage,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock,
            action_storage=action_storage_mock,
            elasticsearch_storage=elasticsearch_storage,
            task_stage_storage=task_stage_storage,
            task_template_storage=task_template_storage,
            create_task_storage=create_task_storage
        )
        return interactor

    def test_invalid_task_display_id_raises_exception(
            self, presenter, task_storage_mock, interactor
    ):
        # Arrange
        task_display_id = "task_1"
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(
            presenter=presenter, task_display_id=task_display_id
        )

        # Assert
        error_obj = presenter.raise_invalid_task_display_id.call_args[0][0]
        invalid_task_display_id = error_obj.task_display_id
        assert invalid_task_display_id == task_display_id

    def test_user_not_in_project_exception(
            self, presenter, task_storage_mock, interactor, storage,
            user_in_project_mock
    ):
        # Arrange
        task_display_id = "task_1"
        task_id = 1
        user_id = "user_1"
        project_id = "FIN_MAN"
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_storage_mock.get_project_id_for_the_task_id.return_value = project_id
        storage.validate_task_id.return_value = True
        user_in_project_mock.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        presenter.get_response_for_user_not_in_project.assert_called_once()
        user_in_project_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )

    @pytest.fixture()
    def gof_name_dto(self):
        GoFIdWithGoFDisplayNameDTOFactory.reset_sequence(1)
        gof_name_dtos = GoFIdWithGoFDisplayNameDTOFactory.create_batch(2)
        return gof_name_dtos

    @pytest.fixture()
    def field_name_dtos(self):
        FieldIdWithFieldDisplayNameDTOFactory.reset_sequence(1)
        field_dtos = FieldIdWithFieldDisplayNameDTOFactory.create_batch(2)
        return field_dtos

    def set_up_storage_for_required_fields(
            self, bool_field, task_storage_mock, action_storage_mock,
            storage, user_in_project_mock, user_project_roles_mock,
            user_roles, gof_storage, gof_name_dto, field_storage, field_name_dtos
    ):
        task_id = 1
        project_id = "FINMAN"
        task_storage_mock.check_is_valid_task_display_id.return_value = bool_field
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_storage_mock.get_project_id_for_the_task_id.return_value = project_id
        storage.validate_task_id.return_value = bool_field
        user_in_project_mock.return_value = bool_field
        action_storage_mock.get_action_type_for_given_action_id\
            .return_value = None
        user_in_project_mock.return_value = user_roles
        gof_storage.get_user_write_permitted_gof_ids_in_given_gof_ids\
            .return_value = gof_name_dto
        field_storage.get_user_write_permitted_field_ids_for_given_gof_ids\
            .return_value = field_name_dtos

    def test_invalid_template_fields(
            self, interactor, presenter, task_storage_mock,
            action_storage_mock, storage, user_in_project_mock,
            user_project_roles_mock, create_task_storage,
            task_template_storage, gof_storage, gof_name_dto,
            field_storage, field_name_dtos
    ):
        # Arrange
        # TODO need to write validation for unfilled fields
        pass

    @staticmethod
    @pytest.fixture()
    def set_up_storage_for_invalid_board(
            storage, task_storage_mock,
            user_in_project_mock, action_storage_mock
    ):
        task_id = 1
        project_id = "FIN_MAN"
        storage.validate_task_id.return_value = True
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_storage_mock.get_project_id_for_the_task_id \
            .return_value = project_id
        user_in_project_mock.return_value = True
        validation_type = ActionTypes.NO_VALIDATIONS.value
        action_storage_mock.get_action_type_for_given_action_id \
            .return_value = validation_type

    @staticmethod
    @pytest.fixture()
    def invalid_board_mock(mocker):
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService'
            '.validate_board_id'
        )
        mock_obj.return_value = False
        return mock_obj

    @staticmethod
    @pytest.fixture()
    def valid_board_mock(mocker):
        mock_obj = mocker.patch(
            'ib_tasks.adapters.boards_service.BoardsService'
            '.validate_board_id'
        )
        mock_obj.return_value = True
        return mock_obj

    def test_invalid_board_raises_exception(
            self, presenter, interactor,
            set_up_storage_for_invalid_board,
            invalid_board_mock
    ):
        # Arrange
        board_id = "board_1"
        task_display_id = "task_1"

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        invalid_board_mock.assert_called_once_with(board_id=board_id)
        dict_obj = presenter.raise_exception_for_invalid_board.call_args.kwargs
        expected_board_id = dict_obj['error_obj'].board_id
        assert board_id == expected_board_id

    def test_invalid_action_raises_exception(
            self, presenter, interactor,
            valid_board_mock, storage,
            set_up_storage_for_invalid_board
    ):
        # Arrange
        task_display_id = "task_1"
        action_id = 1
        storage.validate_action.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        storage.validate_action.assert_called_once_with(action_id=action_id)
        dict_obj = \
            presenter.raise_exception_for_invalid_action.call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    @staticmethod
    @pytest.fixture()
    def invalid_action_roles_mock(mocker):
        path = 'ib_tasks.interactors.user_role_validation_interactor' \
               '.UserRoleValidationInteractor' \
               '.does_user_has_required_permission'
        validation_mock_obj = mocker.patch(path)
        validation_mock_obj.return_value = False
        return validation_mock_obj

    def test_given_user_permission_denied_raises_exception(
            self, presenter, interactor,
            valid_board_mock, storage,
            set_up_storage_for_invalid_board,
            invalid_action_roles_mock
    ):

        # Arrange
        task_display_id = "task_1"
        action_id = 1
        user_id = "user_1"
        project_id = "FIN_MAN"
        storage.validate_action.return_value = True
        action_roles = ["ROLE_2", "ROLE_4"]
        storage.get_action_roles.return_value = action_roles

        # Act
        interactor.user_action_on_task_wrapper(presenter=presenter,
                                               task_display_id=task_display_id)

        # Assert
        invalid_action_roles_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id, role_ids=action_roles
        )
        dict_obj = \
            presenter.raise_exception_for_user_action_permission_denied \
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    @staticmethod
    @pytest.fixture()
    def valid_action_roles_mock(mocker):
        path = 'ib_tasks.interactors.user_role_validation_interactor' \
               '.UserRoleValidationInteractor' \
               '.does_user_has_required_permission'
        validation_mock_obj = mocker.patch(path)
        validation_mock_obj.return_value = True
        return validation_mock_obj

    @pytest.fixture()
    def current_board_mock(self, mocker):
        path = \
            'ib_tasks.interactors.user_action_on_task' \
            '.get_task_current_board_complete_details_interactor' \
            '.GetTaskCurrentBoardCompleteDetailsInteractor' \
            '.get_task_current_board_complete_details'
        return mocker.patch(path)

    @staticmethod
    @pytest.fixture()
    def set_up_storage_for_due_date_missed(
            set_up_storage_for_invalid_board, action_storage_mock,
            task_storage_mock, storage, valid_action_roles_mock

    ):
        action_storage_mock.get_stage_id_for_given_action_id.return_value = 1
        storage.validate_action.return_value = True

    def test_when_due_date_is_missed_but_reason_and_due_date_is_not_updated_raises_exception(
            self, presenter, interactor,
            valid_board_mock, storage,
            set_up_storage_for_due_date_missed,
            valid_action_roles_mock, assignees,
            task_storage_mock, create_task_storage
    ):
        # Arrange
        task_display_id = "task_1"
        create_task_storage.get_existing_task_due_date.return_value = \
            datetime.datetime.now() - datetime.timedelta(days=1)
        create_task_storage.check_task_delay_reason_updated_or_not.return_value = False

        # Act
        interactor.user_action_on_task_wrapper(
            presenter=presenter, task_display_id=task_display_id
        )

        # Assert
        presenter.get_response_for_task_delay_reason_not_updated.\
            assert_called_once()

    @staticmethod
    @pytest.fixture()
    def set_up_invalid_present_stage_action(
            create_task_storage, set_up_storage_for_due_date_missed,
            valid_action_roles_mock
    ):
        create_task_storage.get_existing_task_due_date.return_value = \
            datetime.datetime.now() - datetime.timedelta(days=1)
        create_task_storage.check_task_delay_reason_updated_or_not.return_value = True

    def test_invalid_present_stage_action_raises_exception(
            self, interactor, presenter, storage,
            set_up_invalid_present_stage_action
    ):
        # Arrange
        task_display_id = "task_1"
        action_id = 1
        action_ids = [2, 3, 4]
        storage.get_task_present_stage_actions.return_value = action_ids

        # Act
        interactor.user_action_on_task_wrapper(
            presenter=presenter, task_display_id=task_display_id
        )

        # Assert
        dict_obj = presenter.raise_exception_for_invalid_present_actions \
            .call_args.kwargs
        expected_action_id = dict_obj['error_obj'].action_id
        assert action_id == expected_action_id

    @staticmethod
    @pytest.fixture()
    def set_up_storage_for_valid_case(
        set_up_invalid_present_stage_action, storage,
        get_task_current_stages_mock,
    ):
        action_ids = [1, 2, 3, 4]
        storage.get_task_present_stage_actions.return_value = action_ids

    @staticmethod
    @pytest.fixture()
    def call_action_mock(mocker):
        path = "ib_tasks.interactors.user_action_on_task" \
               ".call_action_logic_function_and_get_or_update_task_status_variables_interactor" \
               ".CallActionLogicFunctionAndGetOrUpdateTaskStatusVariablesInteractor" \
               ".call_action_logic_function_and_update_task_status_variables"
        mock_obj = mocker.patch(path)
        return mock_obj

    @staticmethod
    @pytest.fixture()
    def task_dto():
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=1),
            TaskGoFDTOFactory(task_gof_id=3, gof_id="gof2", same_gof_order=2),
        ]
        gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=3)
        task_dto = TaskDetailsDTOFactory(
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=gof_field_dtos
        )
        return task_dto

    @pytest.fixture()
    def task_complete_details(self, assignees):
        task_display_id = "task_1"
        task_id = 1
        task_complete_details = self.prepare_task_complete_details(
            task_id=task_id, assignees=assignees,
            task_display_id=task_display_id
        )
        return task_complete_details

    @staticmethod
    @pytest.fixture()
    def satisfied_stages_mock(mocker):
        path = 'ib_tasks.interactors.user_action_on_task.get_task_stage_logic_satisfied_stages' \
               '.GetTaskStageLogicSatisfiedStagesInteractor' \
               '.get_task_stage_logic_satisfied_stages'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_given_valid_details_returns_task_complete_details(
            self, presenter, interactor,
            valid_board_mock, storage,
            set_up_storage_for_valid_case,
            valid_action_roles_mock, assignees,
            get_task_current_stages_mock, filtered_task_overview_user,
            current_board_mock, random_assignee_mock,
            call_action_mock, task_dto, task_complete_details,
            satisfied_stages_mock, create_task_storage
    ):
        # Arrange
        user_id = "user_1"
        task_display_id = "task_1"
        task_id = 1
        project_id = "FIN_MAN"
        view_type = ViewType.KANBAN.value
        create_task_storage.get_existing_task_due_date.return_value = \
            datetime.datetime.now() + datetime.timedelta(days=1)
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        get_task_current_stages_mock.return_value = \
            task_current_stages_details
        filtered_task_overview_user.return_value = None
        current_board_mock.return_value = task_complete_details
        stage_ids = ['stage_1', 'stage_2']
        satisfied_stages_mock.return_value = stage_ids

        # Act
        interactor.user_action_on_task_wrapper(
            presenter=presenter, task_display_id=task_display_id
        )

        # Assert
        call_action_mock.assert_called_once()
        storage.update_task_stages.assert_called_once_with(
            stage_ids=stage_ids, task_id=task_id
        )
        satisfied_stages_mock.assert_called_once()
        filtered_task_overview_user.assert_called_once_with(
            view_type=view_type, user_id=user_id,
            task_ids=[task_id], project_id=project_id
        )
        random_assignee_mock.assert_called_once_with(
            task_id=task_id, stage_ids=stage_ids
        )
        current_board_mock.assert_called_once_with(
            task_id=task_id, stage_ids=stage_ids
        )
        presenter.get_response_for_user_action_on_task.assert_called_once_with(
                task_complete_details_dto=task_complete_details,
                task_current_stage_details_dto=task_current_stages_details,
                all_tasks_overview_dto=None
        )
