import pytest

from ib_tasks.models import TaskStageHistory
from ib_tasks.tests.factories.interactor_dtos import \
    TaskIdWithStageAssigneeDTOFactory
from ib_tasks.tests.factories.models import TaskFactory, StageModelFactory, \
    CurrentTaskStageModelFactory


@pytest.mark.django_db
class TestTaskStageAssignees:
    @pytest.fixture
    def task_id_with_stage_assignee_dtos(self):
        TaskIdWithStageAssigneeDTOFactory.reset_sequence()
        return TaskIdWithStageAssigneeDTOFactory.create_batch(3, task_id=1)

    @pytest.fixture
    def populate_data(self):
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskFactory.create_batch(3)
        StageModelFactory.create_batch(3)

    @pytest.fixture
    def task_stage_objs(self):
        TaskFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        task_obj = TaskFactory()
        CurrentTaskStageModelFactory.create_batch(3, task=task_obj)

    def test_create_task_stage_assignees(self,
                                         task_id_with_stage_assignee_dtos,
                                         populate_data):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        # Act
        storage.create_task_stage_assignees(
            task_id_with_stage_assignee_dtos)
        # Assert
        for each_task_id_with_stage_assignee_dto in \
                task_id_with_stage_assignee_dtos:
            task_stage_obj = TaskStageHistory.objects.get(
                task_id=each_task_id_with_stage_assignee_dto.task_display_id,
                stage_id=each_task_id_with_stage_assignee_dto.db_stage_id
            )
            assert task_stage_obj.task_display_id == \
                   each_task_id_with_stage_assignee_dto.task_display_id
            assert task_stage_obj.stage_id == \
                   each_task_id_with_stage_assignee_dto.db_stage_id
            assert task_stage_obj.assignee_id == \
                   each_task_id_with_stage_assignee_dto.assignee_id