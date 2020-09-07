import factory
import pytest

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskTemplateStageDTO
from ib_tasks.models import CurrentTaskStage
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


class TaskTemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStageDTO

    task_template_id = factory.sequence(lambda n: "task_template_id_%d" % n)
    stage_id = factory.Sequence(lambda n: n)


@pytest.mark.django_db
class TestCreateInitialStages:

    def test_creates_initial_stages_for_given_task_template_ids(
            self, task_template_stages_dtos):
        # Arrange
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        storage = StagesStorageImplementation()

        # Act
        storage.create_initial_stage_to_task_template(
            task_template_stages_dtos)

        # Assert
        task_stages = CurrentTaskStage.objects.filter(
            task__template_id__in=task_template_ids)
        self._validate_task_stage_objects(
            task_stages, task_template_stages_dtos)

    @staticmethod
    def _validate_task_stage_objects(returned, expected):
        if len(returned) != len(expected):
            for val in range(len(returned)):
                assert returned[val].task_template_id == expected[
                    val].task_template_id
                assert returned[val].stage__stage_id == expected[val].stage_id
        else:
            assert len(returned) == len(expected)