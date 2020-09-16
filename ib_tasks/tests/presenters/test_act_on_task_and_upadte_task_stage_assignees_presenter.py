import datetime
import json

import pytest


class TestActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters. \
            act_on_task_and_upadte_task_stage_assignees_presenter import \
            ActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation
        return ActOnTaskAndUpdateTaskStageAssigneesPresenterImplementation()

    def test_raise_exception_for_invalid_task_display_id(
            self, presenter, snapshot
    ):
        # Arrange
        task_display_id = "IBWF_1"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        error = InvalidTaskDisplayId(task_display_id=task_display_id)

        # Act
        response_object = \
            presenter.raise_invalid_task_display_id(err=error)

        # Assert
        snapshot.assert_match(
            name="invalid_task", value=json.loads(response_object.content)
        )

    def test_raise_exception_for_invalid_board(
            self, presenter, snapshot
    ):
        # Arrange
        board_id = "board_1"

        from ib_tasks.interactors.user_action_on_task. \
            user_action_on_task_interactor import \
            InvalidBoardIdException
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

    def test_raise_user_did_not_fill_required_fields(
            self, presenter, snapshot
    ):
        # Arrange
        field_display_name = "field_display_1"
        field_id = "field_1"
        gof_display_name = "gof_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields
        from ib_tasks.interactors.storage_interfaces.fields_dtos import \
            FieldIdWithFieldDisplayNameDTO
        error = UserDidNotFillRequiredFields(unfilled_field_dtos=[
            FieldIdWithFieldDisplayNameDTO(
                field_display_name=field_display_name, field_id=field_id,
                gof_display_name=gof_display_name)])

        # Act
        response_object = \
            presenter.raise_user_did_not_fill_required_fields(err=error)

        # Assert
        snapshot.assert_match(
            name="required fields are not filled by user", value=json.loads(
                response_object.content)
        )

    def test_raise_exception_for_invalid_present_actions(
            self, presenter, snapshot):
        # Arrange
        action_id = 1

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        error = InvalidPresentStageAction(action_id=action_id)

        # Act
        response_object = \
            presenter.raise_exception_for_invalid_present_actions(
                error_obj=error)

        # Assert
        snapshot.assert_match(
            name="invalid present stage action",
            value=json.loads(response_object.content)
        )
    def test_raise_user_not_in_project(
            self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.adapter_exceptions import \
            UserIsNotInProjectException
        error = UserIsNotInProjectException()

        # Act
        response_object = \
            presenter.get_response_for_user_not_in_project()

        # Assert
        snapshot.assert_match(
            name="user not in project",
            value=json.loads(response_object.content)
        )

    def test_with_duplicate_stage_ids(self, presenter, snapshot):
        # Arrange
        duplicate_stage_ids = [2, 2]
        # Act
        response_object = presenter.raise_duplicate_stage_ids_not_valid(
            duplicate_stage_ids=duplicate_stage_ids)
        # Assert
        snapshot.assert_match(
            name="duplicate stage ids",
            value=json.loads(response_object.content)
        )

    def test_given_invalid_stage_ids_raise_exception(self, presenter,
                                                     snapshot):
        # Arrange
        invalid_stage_ids = [1, 2]
        # Act
        response_object = presenter.raise_invalid_stage_ids_exception(
            invalid_stage_ids=invalid_stage_ids)
        # Assert
        snapshot.assert_match(
            name="invalid stage ids",
            value=json.loads(response_object.content))

    def test_given_virtual_stage_ids_raise_exception(self, presenter,
                                                    snapshot):
        # Arrange
        virtual_stage_ids = [1, 2]
        # Act
        response_object = presenter.raise_virtual_stage_ids_exception(
            virtual_stage_ids=virtual_stage_ids)
        # Assert
        snapshot.assert_match(
            name="virtual stage ids",
            value=json.loads(response_object.content)
        )

    def test_raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, presenter, snapshot):
        # Arrange
        invalid_stage_ids = [1, 2]
        # Act
        response_object = presenter. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception(
            invalid_stage_ids=invalid_stage_ids)
        # Assert
        snapshot.assert_match(
            name="stage ids with invalid permission for assignee",
            value=json.loads(response_object.content)
        )



    @pytest.fixture()
    def task_complete_details(self, reset_sequence):
        from ib_tasks.tests.factories.adapter_dtos import ColumnStageDTOFactory
        column_stage_dtos = ColumnStageDTOFactory.create_batch(size=3)

        from ib_tasks.adapters.dtos import TaskBoardsDetailsDTO
        from ib_tasks.tests.factories.adapter_dtos import BoardDTOFactory
        from ib_tasks.tests.factories.adapter_dtos import ColumnDTOFactory
        task_board_details = TaskBoardsDetailsDTO(
                board_dto=BoardDTOFactory(),
                column_stage_dtos=column_stage_dtos,
                columns_dtos=ColumnDTOFactory.create_batch(size=3)
        )
        from ib_tasks.tests.factories.interactor_dtos import \
            FieldDisplayDTOFactory
        field_dtos = FieldDisplayDTOFactory.create_batch(size=3)
        field_dto = field_dtos[1]
        field_dto.stage_id = 'stage_2'
        field_dtos.append(field_dto)
        from ib_tasks.tests.factories.adapter_dtos import \
            AssigneeDetailsDTOFactory
        assignee_dtos = [AssigneeDetailsDTOFactory()]
        from ib_tasks.interactors.presenter_interfaces.dtos import \
            TaskCompleteDetailsDTO
        from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskStageDTOFactory
        return TaskCompleteDetailsDTO(
                task_id=1,
                task_boards_details=task_board_details,
                actions_dto=ActionDTOFactory.create_batch(size=3),
                field_dtos=field_dtos,
                assignees_details=[],
                task_stage_details=TaskStageDTOFactory.create_batch(3),
                task_display_id=''
        )

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.adapter_dtos import ColumnDTOFactory
        ColumnDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.adapter_dtos import BoardDTOFactory
        BoardDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.adapter_dtos import ColumnStageDTOFactory
        ColumnStageDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory
        ActionDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.interactor_dtos import \
            FieldDisplayDTOFactory
        FieldDisplayDTOFactory.reset_sequence(0)
        from ib_tasks.tests.factories.presenter_dtos \
            import AllTasksOverviewDetailsDTOFactory
        AllTasksOverviewDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.presenter_dtos \
            import TaskIdWithStageDetailsDTOFactory
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            AssigneeWithTeamDetailsDTOFactory
        AssigneeWithTeamDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskStageAssigneeDetailsDTOFactory
        TaskStageAssigneeDetailsDTOFactory.reset_sequence()

    def test_get_response_for_user_action_on_task(
            self, presenter, snapshot, task_complete_details, reset_sequence
    ):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskCurrentStageDetailsDTOFactory
        TaskCurrentStageDetailsDTOFactory.reset_sequence(1)
        task_current_stage_details_dto = TaskCurrentStageDetailsDTOFactory()
        from ib_tasks.tests.factories.presenter_dtos import \
            AllTasksOverviewDetailsDTOFactory
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
