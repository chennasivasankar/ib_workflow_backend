import json

import pytest

from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.tests.factories.adapter_dtos import (
    ColumnStageDTOFactory, BoardDTOFactory, ColumnDTOFactory
)
from ib_tasks.tests.factories.interactor_dtos import FieldDisplayDTOFactory, \
    TaskCurrentStageDetailsDTOFactory
from ib_tasks.tests.factories.interactor_dtos import TaskStageDTOFactory
from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory


class TestCreateOrUpdateTaskPresenterImplementation:

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

        from ib_tasks.interactors.user_action_on_task_interactor \
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
            name="invalid_action", value=json.loads(response_object.content)
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

    def reset_sequence(self):
        ColumnDTOFactory.reset_sequence(0)
        BoardDTOFactory.reset_sequence(0)
        ColumnStageDTOFactory.reset_sequence(0)
        ActionDTOFactory.reset_sequence(0)
        FieldDisplayDTOFactory.reset_sequence(0)

    @pytest.fixture()
    def task_complete_details(self):
        self.reset_sequence()
        column_stage_dtos = ColumnStageDTOFactory.create_batch(size=3)
        ColumnStageDTOFactory.reset_sequence(0)

        task_board_details = TaskBoardsDetailsDTO(
            board_dto=BoardDTOFactory(),
            column_stage_dtos=column_stage_dtos,
            columns_dtos=ColumnDTOFactory.create_batch(size=3)
        )
        return TaskCompleteDetailsDTO(
            task_id=1,
            task_boards_details=task_board_details,
            actions_dto=ActionDTOFactory.create_batch(size=3),
            field_dtos=FieldDisplayDTOFactory.create_batch(size=3),
            assignees_details=[],
            task_stage_details=TaskStageDTOFactory.create_batch(3)
        )

    def test_get_response_for_user_action_on_task(
            self, presenter, snapshot, task_complete_details
    ):
        # Arrange
        task_current_stage_details_dto = TaskCurrentStageDetailsDTOFactory()

        # Act
        response_object = \
            presenter.get_response_for_user_action_on_task(
                task_complete_details_dto=task_complete_details,
                task_current_stage_details_dto=task_current_stage_details_dto
            )

        # Assert
        snapshot.assert_match(
            name="task_complete_details",
            value=json.loads(response_object.content)
        )
