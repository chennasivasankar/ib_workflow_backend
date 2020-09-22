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
        task_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        return task_ids

    @pytest.fixture
    def task_base_details_dtos(self, task_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=15
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
    def task_stage_complete_details_dtos(self, task_ids):
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
                task_id=factory.Iterator(task_ids),
                field_dtos=FieldDetailsDTOFactory.create_batch(size=3),
                action_dtos=StageActionDetailsDTOFactory.create_btach(size=1)
            )
        return task_stage_complete_details_dtos




    def test_given_group_details_dtos_and_task_details_dtos_returns_group_info_task_details_dtos(
            self
    ):
        # Arrange

        pass
        # Act

        # Arrange
