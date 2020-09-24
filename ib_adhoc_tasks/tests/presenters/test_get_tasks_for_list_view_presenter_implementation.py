import factory
import pytest


class TestGetTasksForListViewPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_tasks_for_list_view_presenter_implementation import \
            GetTasksForListViewPresenterImplementation
        return GetTasksForListViewPresenterImplementation()

    @pytest.fixture
    def task_ids(self):
        task_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        return task_ids

    @pytest.fixture
    def task_base_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence(0)
        from ib_adhoc_tasks.constants.enum import Priority
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=15, priority=Priority.HIGH.value
        )
        return task_base_details_dtos

    @pytest.fixture
    def stage_ids(self):
        stage_ids = [
            "stage1", "stage2", "stage3", "stage4", "stage5", "stage6",
            "stage7", "stage8", "stage9", "stage10", "stage11", "stage12",
            "stage13", "stage14", "stage15"
        ]
        return stage_ids

    @pytest.fixture
    def task_stage_complete_details_dtos(self, task_ids, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            GetTaskStageCompleteDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            StageActionDetailsDTOFactory
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence(0)
        FieldDetailsDTOFactory.reset_sequence(0)
        StageActionDetailsDTOFactory.reset_sequence(0)
        task_stage_complete_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory.create_batch(
                size=15,
                field_dtos=FieldDetailsDTOFactory.create_batch(size=3),
                stage_id=factory.Iterator(stage_ids),
                action_dtos=StageActionDetailsDTOFactory.create_batch(
                    size=1, stage_id=factory.Iterator(stage_ids)
                )
            )
        return task_stage_complete_details_dtos

    @pytest.fixture
    def task_stage_assignee_details_dto(self, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskStageAssigneeDetailsDTOFactory, AssigneeDetailsDTOFactory, \
            TeamDetailsDTOFactory
        TaskStageAssigneeDetailsDTOFactory.reset_sequence(0)
        AssigneeDetailsDTOFactory.reset_sequence(0)
        TeamDetailsDTOFactory.reset_sequence(0)
        task_stage_assignee_details_dto = \
            TaskStageAssigneeDetailsDTOFactory.create_batch(
                size=15,
                stage_id=factory.Iterator(stage_ids)
            )
        return task_stage_assignee_details_dto

    @pytest.fixture
    def task_complete_details_dto(
            self, task_base_details_dtos, task_stage_complete_details_dtos,
            task_stage_assignee_details_dto
    ):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        TasksCompleteDetailsDTOFactory.reset_sequence(0)
        task_complete_details_dto = TasksCompleteDetailsDTOFactory(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_details_dtos=task_stage_complete_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_details_dto
        )
        return task_complete_details_dto

    @pytest.fixture
    def group_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupDetailsDTOFactory
        GroupDetailsDTOFactory.reset_sequence(0)
        group_details_dtos = GroupDetailsDTOFactory.create_batch(
            size=3, total_tasks=5
        )
        return group_details_dtos

    @pytest.fixture()
    def sub_tasks_count_dtos(self, task_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskIdWithSubTasksCountDTOFactory
        TaskIdWithSubTasksCountDTOFactory.reset_sequence(0)
        sub_tasks_count_dtos = TaskIdWithSubTasksCountDTOFactory.create_batch(
            size=16, task_id=factory.Iterator(task_ids)
        )
        return sub_tasks_count_dtos

    @pytest.fixture()
    def completed_sub_tasks_count_dtos(self, task_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskIdWithCompletedSubTasksCountDTOFactory
        TaskIdWithCompletedSubTasksCountDTOFactory.reset_sequence(0)
        completed_sub_tasks_count_dtos = \
            TaskIdWithCompletedSubTasksCountDTOFactory \
            .create_batch(size=16, task_id=factory.Iterator(task_ids))
        return completed_sub_tasks_count_dtos

    def test_raise_invalid_offset_value(self, snapshot, presenter):
        # Arrange

        # Act
        response = presenter.raise_invalid_offset_value()

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response.content
        )

    def test_raise_invalid_limit_value(self, snapshot, presenter):
        # Arrange

        # Act
        response = presenter.raise_invalid_limit_value()

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response.content
        )

    def test_raise_invalid_project_id(self, snapshot, presenter):
        # Arrange

        # Act
        response = presenter.raise_invalid_project_id()

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response.content
        )

    def test_raise_invalid_user_id(self, snapshot, presenter):
        # Arrange

        # Act
        response = presenter.raise_invalid_user_id()

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response.content
        )

    def test_raise_invalid_user_for_project(self, snapshot, presenter):
        # Arrange

        # Act
        response = presenter.raise_invalid_user_for_project()

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response.content
        )

    @pytest.fixture
    def task_details_with_group_info_list_view_dto(
            self, group_details_dtos, task_complete_details_dto,
            sub_tasks_count_dtos, completed_sub_tasks_count_dtos
    ):
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .get_tasks_for_list_view_presenter_interface import \
            TaskDetailsWithGroupInfoForListViewDTO
        total_groups_count = 3
        task_details_with_group_info_list_view_dto = \
            TaskDetailsWithGroupInfoForListViewDTO(
                group_details_dtos=group_details_dtos,
                task_details_dto=task_complete_details_dto,
                total_groups_count=total_groups_count,
                task_with_sub_tasks_count_dtos=sub_tasks_count_dtos,
                task_completed_sub_tasks_count_dtos=completed_sub_tasks_count_dtos
            )
        return task_details_with_group_info_list_view_dto

    def test_given_group_details_dtos_and_task_details_dtos_returns_group_info_task_details(
            self, task_complete_details_dto, presenter,
            snapshot, task_details_with_group_info_list_view_dto
    ):
        # Arrange

        # Act
        response = presenter.get_task_details_group_by_info_response(
            task_details_with_group_info_list_view_dto
        )

        # Arrange
        import json
        response = json.loads(response.content)
        response = json.dumps(response, indent=4)
        snapshot.assert_match(
            name="group_by_task_details",
            value=response
        )
