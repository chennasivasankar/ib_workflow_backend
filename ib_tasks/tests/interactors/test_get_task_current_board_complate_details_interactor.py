from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.interactors.user_action_on_task_interactor \
    import UserActionOnTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    TaskCurrentStageDetailsDTOFactory, FieldDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory, \
    StageActionDetailsDTOFactory


class TestUserActionOnTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        ActionDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
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

    @staticmethod
    def task_boards_mock(mocker, task_board_details):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_board_details
        return mock_obj

    @pytest.fixture
    def assignees(self):
        from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
        from ib_tasks.adapters.dtos import AssigneeDetailsDTO
        return TaskStageAssigneeDetailsDTO(
            task_id=1,
            stage_id='stage_id_1',
            assignee_details=AssigneeDetailsDTO(assignee_id='1', name='name',
                                                profile_pic_url='pavan.com')
        )

    @pytest.fixture()
    def assignees_mock(self, mocker):

        path = 'ib_tasks.interactors.get_stages_assignees_details_interactor.GetStagesAssigneesDetailsInteractor' \
               '.get_stages_assignee_details_by_given_task_ids'
        return mocker.patch(path)

    @staticmethod
    def prepare_task_complete_details(task_id, assignees,
                                      task_boards_details,
                                      task_display_id, field_dtos,
                                      action_dtos):
        from ib_tasks.interactors.presenter_interfaces.dtos \
            import TaskCompleteDetailsDTO
        from ib_tasks.interactors.stage_dtos import TaskStageDTO
        return TaskCompleteDetailsDTO(
            task_id=task_id,
            task_display_id=task_display_id,
            task_boards_details=task_boards_details,
            actions_dto=action_dtos,
            field_dtos=field_dtos,
            assignees_details=[assignees],
            task_stage_details=[TaskStageDTO(stage_id='stage_1', db_stage_id=1,
                                             display_name='stage',
                                             stage_colour='color_1')]
        )

    @pytest.fixture()
    def task_fields_actions_mock(self, mocker):
        path = 'ib_tasks.interactors.get_task_fields_and_actions' \
               '.get_task_fields_and_actions.GetTaskFieldsAndActionsInteractor' \
               '.get_task_fields_and_action'
        mock_obj = mocker.patch(path)
        return mock_obj

    def test_given_valid_details_returns_task_complete_details(
            self, mocker, storage, presenter,
            task_stage_storage, assignees, task_fields_actions_mock,
            field_storage, stage_storage, board_mock,
            task_storage_mock, action_storage_mock
    ):
        # Arrange
        user_id = "1"
        board_id = "board_1"
        task_display_id = "task_1"
        task_id = 1
        task_storage_mock.get_task_display_id_for_task_id.return_value = task_display_id
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value
        from ib_tasks.interactors.get_task_current_board_complete_details_interactor import \
            GetTaskCurrentBoardCompleteDetailsInteractor
        interactor = GetTaskCurrentBoardCompleteDetailsInteractor(
            user_id=user_id, board_id=board_id,
            field_storage=field_storage, stage_storage=stage_storage,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage, view_type=view_type
        )
        from ib_tasks.tests.common_fixtures.interactors import (
            prepare_task_boards_details,
            prepare_assignees_interactor_mock
        )
        assignee_mock = prepare_assignees_interactor_mock(mocker)
        assignee_mock.return_value = [assignees]

        task_board_details = prepare_task_boards_details()
        board_mock.return_value = task_board_details
        stage_ids = ['stage_1']
        FieldDetailsDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.presenter_dtos \
            import GetTaskStageCompleteDetailsDTOFactory
        field_dto = FieldDetailsDTOFactory()
        action_dto = StageActionDetailsDTOFactory(stage_id='stage_1')
        task_fields_actions = GetTaskStageCompleteDetailsDTOFactory(
            task_id=task_id,
            field_dtos=[field_dto],
            action_dtos=[action_dto]
        )
        task_fields_actions_mock.return_value = [task_fields_actions]
        from ib_tasks.tests.factories.storage_dtos \
            import ActionDTOFactory
        ActionDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos \
            import FieldDisplayDTOFactory
        FieldDisplayDTOFactory.reset_sequence()
        field_dtos = [FieldDisplayDTOFactory(
            field_id=field_dto.field_id,
            stage_id="stage_1",
            field_type=field_dto.field_type,
            key=field_dto.key,
            value=field_dto.value
        )]
        action_dtos = [ActionDTOFactory(
            action_id=action_dto.action_id,
            action_type=action_dto.action_type,
            name=action_dto.name,
            transition_template_id=action_dto.transition_template_id,
            stage_id=action_dto.stage_id,
            button_text=action_dto.button_text,
            button_color=action_dto.button_color
        )]
        task_complete_details = self.prepare_task_complete_details(
            task_id=task_id, task_boards_details=task_board_details,
            assignees=assignees, task_display_id=task_display_id,
            field_dtos=field_dtos, action_dtos=action_dtos
        )

        # Act
        response = interactor.get_task_current_board_complete_details(
            task_id=task_id, stage_ids=stage_ids
        )

        # Assert
        assert response == task_complete_details
