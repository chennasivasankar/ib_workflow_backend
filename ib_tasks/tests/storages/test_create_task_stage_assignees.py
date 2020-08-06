import pytest

from ib_tasks.models import TaskStage
from ib_tasks.tests.factories.interactor_dtos import \
    TaskIdWithStageAssigneeDTOFactory


@pytest.mark.django_db
class TestTaskStageAssignees:
    @pytest.fixture
    def task_id_with_stage_assignee_dtos(self):
        TaskIdWithStageAssigneeDTOFactory.reset_sequence()
        return TaskIdWithStageAssigneeDTOFactory.create_batch(3)

    def test_create_task_stage_assignees(self,
                                         task_id_with_stage_assignee_dtos):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        # Act
        storage.create_task_stage_assignees(
            task_id_with_stage_assignee_dtos)
        # Assert
        for each_task_id_with_stage_assignee_dto in task_id_with_stage_assignee_dtos:
            task_stage_obj = TaskStage.objects.get(
                task_id=each_task_id_with_stage_assignee_dto.task_id,
                stage__stage_id=each_task_id_with_stage_assignee_dto.stage_id
            )
            assert task_stage_obj.task_id == each_task_id_with_stage_assignee_dto.task_id
            assert task_stage_obj.stage__stage_id == each_task_id_with_stage_assignee_dto.stage_id
            assert task_stage_obj.stage_assignee == each_task_id_with_stage_assignee_dto.assignee_id
