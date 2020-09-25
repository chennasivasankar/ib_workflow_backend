import factory
import pytest


class TestGetTasksForKanbanViewPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_tasks_for_kanban_view_presenter_implementation import \
            GetTasksForKanbanViewPresenterImplementation
        return GetTasksForKanbanViewPresenterImplementation()

    @pytest.fixture
    def task_base_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=15
        )
        return task_base_details_dtos

    @pytest.fixture
    def task_ids(self):
        task_ids = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
        return task_ids

    @pytest.fixture
    def task_base_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=12
        )
        return task_base_details_dtos

    @pytest.fixture
    def stage_ids(self):
        stage_ids = [
            "stage1", "stage2", "stage3", "stage4", "stage5", "stage6",
            "stage7", "stage8", "stage9", "stage10", "stage11", "stage12"
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
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        task_stage_complete_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory.create_batch(
                size=12,
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
            TaskStageAssigneeDetailsDTOFactory
        TaskStageAssigneeDetailsDTOFactory.reset_sequence()
        task_stage_assignee_details_dto = \
            TaskStageAssigneeDetailsDTOFactory.create_batch(
                size=12,
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
        task_complete_details_dto = TasksCompleteDetailsDTOFactory(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_details_dtos=task_stage_complete_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_details_dto
        )
        return task_complete_details_dto

    @pytest.fixture
    def group_by_values(self):
        group_by_values = ["group_by_value1", "group_by_value2"]
        return group_by_values

    @pytest.fixture
    def child_group_count_dtos(self, group_by_values):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            ChildGroupCountDTOFactory
        return ChildGroupCountDTOFactory.create_batch(
            group_by_value=factory.Iterator(group_by_values),
            total_child_groups=2, size=2
        )

    @pytest.fixture
    def group_details_dtos(self, task_ids):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupDetailsDTOFactory
        group_by_values = ["group_by_value1", "group_by_value2"]
        group_by_display_name = ["group_by_display_name", "group_by_display_name"]

        group_details_dtos = GroupDetailsDTOFactory.create_batch(
            size=2, total_tasks=3,
            task_ids=factory.Iterator(task_ids),
            group_by_value=factory.Iterator(group_by_values),
            group_by_display_name=factory.Iterator(group_by_display_name)
        )
        return group_details_dtos

    @pytest.fixture
    def task_details_with_group_by_info_dto(
            self, group_details_dtos, child_group_count_dtos,
            task_complete_details_dto
    ):
        from ib_adhoc_tasks.interactors.presenter_interfaces\
            .get_tasks_for_kanban_view_presenter_interface import \
            TaskDetailsWithGroupByInfoDTO
        task_details_with_group_by_info_dto = TaskDetailsWithGroupByInfoDTO(
            group_details_dtos=group_details_dtos,
            total_groups_count=2,
            child_group_count_dtos=child_group_count_dtos,
            task_details_dtos=task_complete_details_dto
        )
        return task_details_with_group_by_info_dto

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

    def test_given_task_details_group_by_info_dto_returns_group_info_task_details(
            self, task_complete_details_dto, presenter, group_details_dtos,
            snapshot, task_details_with_group_by_info_dto
    ):
        # Arrange

        # Act
        response = presenter.get_task_details_group_by_info_response(
            task_details_with_group_by_info_dto
        )

        # Arrange
        import json
        response = json.loads(response.content)
        response = json.dumps(response, indent=4)
        snapshot.assert_match(
            name="group_by_task_details",
            value=response
        )
