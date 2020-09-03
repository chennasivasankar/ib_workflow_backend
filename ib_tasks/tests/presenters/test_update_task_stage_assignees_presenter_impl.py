import pytest


class TestUpdateTaskStageAssigneesPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.update_task_stage_assignees_presenter_impl \
            import \
            UpdateTaskStageAssigneesPresenterImplementation
        presenter = UpdateTaskStageAssigneesPresenterImplementation()
        return presenter

    def test_given_invalid_task_display_id_raise_exception(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        task_display_id = "BWG-10"
        err = InvalidTaskDisplayId(task_display_id=task_display_id)

        # Act
        response = presenter.raise_invalid_task_display_id(err)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )

    def test_given_duplication_of_stage_ids_raise_exception(
            self, presenter, snapshot
    ):
        # Arrange
        duplicate_stage_ids = [1, 2]

        # Act
        response = presenter.raise_duplicate_stage_ids_not_valid(
            duplicate_stage_ids)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )

    def test_given_invalid_stage_ids_raise_exception(
            self, presenter, snapshot
    ):
        # Arrange
        invalid_stage_ids = [1, 2]

        # Act
        response = presenter.raise_invalid_stage_ids_exception(
            invalid_stage_ids)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )

    def test_given_virtual_stage_ids_raise_exception(
            self, presenter, snapshot
    ):
        # Arrange
        virtual_stage_ids = [1, 2]

        # Act
        response = presenter.raise_virtual_stage_ids_exception(
            virtual_stage_ids)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )

    def test_given_invalid_user_id_raise_exception(
            self, presenter, snapshot
    ):
        # Arrange
        invalid_user_id = "123e4567-e89b-12d3-a456-42661417400"

        # Act
        response = presenter.raise_invalid_user_id_exception(
            invalid_user_id)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )

    def test_given_stage_ids_having_invalid_permission_for_user(
            self, presenter, snapshot
    ):
        # Arrange
        invalid_stage_ids = [1, 2]

        # Act
        response = presenter.raise_stage_ids_with_invalid_permission_for_assignee_exception(
            invalid_stage_ids)

        # Assert
        snapshot.assert_match(
            name="response",
            value=response.content
        )
