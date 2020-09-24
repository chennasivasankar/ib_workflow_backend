import datetime
import json

import pytest

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.tests.factories.adapter_dtos import (
    ColumnStageDTOFactory, BoardDTOFactory, ColumnDTOFactory,
    AssigneeDetailsDTOFactory
)
from ib_tasks.tests.factories.interactor_dtos import (FieldDisplayDTOFactory,
                                                      TaskCurrentStageDetailsDTOFactory,
                                                      AssigneeWithTeamDetailsDTOFactory)
from ib_tasks.tests.factories.interactor_dtos import TaskStageDTOFactory
from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory


class TestCreateOrUpdateTaskPresenterImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskCompleteDetailsDTOFactory, AllTasksOverviewDetailsDTOFactory, \
            TaskBoardsDetailsDTOFactory, TaskIdWithStageDetailsDTOFactory, \
            TaskStageDTOFactory, TaskWithCompleteStageDetailsDTOFactory, \
            GetTaskStageCompleteDetailsDTOFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskStageAssigneeDetailsDTOFactory
        from ib_tasks.tests.factories.storage_dtos import \
            CurrentStageDetailsDTOFactory, ActionDTOFactory, \
            FieldDetailsDTOFactory, StageActionDetailsDTOFactory

        TaskCompleteDetailsDTOFactory.reset_sequence()
        TaskBoardsDetailsDTOFactory.reset_sequence()
        BoardDTOFactory.reset_sequence()
        ActionDTOFactory.reset_sequence()
        FieldDisplayDTOFactory.reset_sequence()
        TaskStageDTOFactory.reset_sequence()
        TaskStageAssigneeDetailsDTOFactory.reset_sequence()
        ColumnStageDTOFactory.reset_sequence()
        ColumnDTOFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()
        CurrentStageDetailsDTOFactory.reset_sequence()
        TaskCurrentStageDetailsDTOFactory.reset_sequence()
        AllTasksOverviewDetailsDTOFactory.reset_sequence()
        TaskWithCompleteStageDetailsDTOFactory.reset_sequence()
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        FieldDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        AssigneeWithTeamDetailsDTOFactory.reset_sequence()

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.user_action_on_task_presenter_implementation \
            import UserActionOnTaskPresenterImplementation
        return UserActionOnTaskPresenterImplementation()

    def test_raise_exception_for_invalid_task(
            self, presenter, snapshot
    ):
        # Arrange
        task_id = 1
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskException
        error = InvalidTaskException(task_id=task_id)

        # Act
        response_object = \
            presenter.raise_exception_for_invalid_task(error_obj=error)

        # Assert
        snapshot.assert_match(
                name="invalid_task", value=json.loads(response_object.content)
        )

    def test_raise_exception_for_invalid_board(
            self, presenter, snapshot
    ):
        # Arrange
        board_id = "board_1"

        from ib_tasks.interactors.user_action_on_task.user_action_on_task_interactor \
            import InvalidBoardIdException
        error = InvalidBoardIdException(board_id=board_id)

        # Act
        response_object = \
            presenter.raise_exception_for_invalid_board(error_obj=error)

        # Assert
        snapshot.assert_match(
                name="invalid_board", value=json.loads(response_object.content)
        )

    def test_raise_exception_for_invalid_action(
            self, presenter, snapshot
    ):
        # Arrange
        action_id = 1

        from ib_tasks.exceptions.action_custom_exceptions \
            import InvalidActionException
        error = InvalidActionException(action_id=action_id)

        # Act
        response_object = \
            presenter.raise_exception_for_invalid_action(error_obj=error)

        # Assert
        snapshot.assert_match(
                name="invalid_action",
                value=json.loads(response_object.content)
        )

    def test_raise_exception_for_invalid_user_permission(
            self, presenter, snapshot
    ):
        # Arrange
        action_id = 1

        from ib_tasks.exceptions.permission_custom_exceptions \
            import UserActionPermissionDenied
        error = UserActionPermissionDenied(action_id=action_id)

        # Act
        response_object = \
            presenter.raise_exception_for_user_action_permission_denied(
                    error_obj=error
            )

        # Assert
        snapshot.assert_match(
                name="invalid_user_permission",
                value=json.loads(response_object.content)
        )

    def test_raise_exception_for_invalid_user_board_permission(
            self, presenter, snapshot
    ):
        # Arrange
        board_id = "board_1"

        from ib_tasks.exceptions.permission_custom_exceptions \
            import UserBoardPermissionDenied
        error = UserBoardPermissionDenied(board_id=board_id)

        # Act
        response_object = \
            presenter.raise_exception_for_user_board_permission_denied(
                    error_obj=error
            )

        # Assert
        snapshot.assert_match(
                name="invalid_user_board_permission",
                value=json.loads(response_object.content)
        )

    @pytest.fixture()
    def task_complete_details(self):
        column_stage_dtos = ColumnStageDTOFactory.create_batch(size=3)

        task_board_details = TaskBoardsDetailsDTO(
                board_dto=BoardDTOFactory(),
                column_stage_dtos=column_stage_dtos,
                columns_dtos=ColumnDTOFactory.create_batch(size=3)
        )
        field_dtos = FieldDisplayDTOFactory.create_batch(size=3)
        field_dto = field_dtos[1]
        field_dto.stage_id = 'stage_2'
        field_dtos.append(field_dto)
        assignee_dtos = [AssigneeDetailsDTOFactory()]
        return TaskCompleteDetailsDTO(
                task_id=1,
                task_boards_details=task_board_details,
                actions_dto=ActionDTOFactory.create_batch(size=3),
                field_dtos=field_dtos,
                assignees_details=[],
                task_stage_details=TaskStageDTOFactory.create_batch(3),
                task_display_id=''
        )

    def test_get_response_for_user_action_on_task(
            self, presenter, snapshot, task_complete_details
    ):
        # Arrange
        from ib_tasks.tests.factories.presenter_dtos \
            import AllTasksOverviewDetailsDTOFactory

        task_current_stage_details_dto = TaskCurrentStageDetailsDTOFactory()
        all_tasks_overview_details = AllTasksOverviewDetailsDTOFactory()

        # Act
        response_object = \
            presenter.get_response_for_user_action_on_task(
                    task_complete_details_dto=task_complete_details,
                    task_current_stage_details_dto
                    =task_current_stage_details_dto,
                    all_tasks_overview_dto=all_tasks_overview_details
            )

        # Assert
        snapshot.assert_match(
                name="task_complete_details",
                value=json.loads(response_object.content)
        )

    def test_raise_exception_for_reason_is_not_added_to_task(
            self, presenter, snapshot
    ):
        # Arrange
        stage_display_name = "PR APPROVALS"
        task_display_id = "IBWF-1"
        updated_due_datetime = datetime.datetime.now()

        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskDelayReasonIsNotUpdated
        error = TaskDelayReasonIsNotUpdated(
                stage_display_name=stage_display_name,
                task_display_id=task_display_id,
                due_date=updated_due_datetime)

        # Act
        response_object = \
            presenter.get_response_for_task_delay_reason_not_updated(err=error)

        # Assert
        snapshot.assert_match(
                name="reason is not added to task delay", value=json.loads(
                        response_object.content)
        )
