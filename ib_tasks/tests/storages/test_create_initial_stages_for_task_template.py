import factory
import pytest

from ib_tasks.interactors.stages_dtos import TemplateStageDTO
from ib_tasks.models import TaskTemplateInitialStage
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


class TaskTemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TemplateStageDTO

    task_template_id = factory.sequence(lambda n: "task_template_id_%d" % n)
    stage_id = factory.Sequence(lambda n: n)


def _validate_task_stage_objs(returned, expected):
    if len(returned) != len(expected):
        for val in range(len(returned)):
            assert returned[val].task_template_id == expected[
                val].task_template_id
            assert returned[val].stage__stage_id == expected[val].stage_id
    else:
        assert len(returned) == len(expected)


@pytest.mark.django_db
class TestCreateInitialStages:

    @pytest.fixture()
    def task_template_stages_dtos(self):
        TaskTemplateStagesDTOFactory.reset_sequence(1)
        return TaskTemplateStagesDTOFactory.create_batch(size=2)

    def test_creates_intital_stages_for_given_task_template_ids(self,
                                                                task_template_stages_dtos):
        # Arrange
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        storage = StagesStorageImplementation()

        # Act
        storage.create_initial_stage_to_task_template(
            task_template_stages_dtos)

        # Assert
        task_stages = TaskTemplateInitialStage.objects.filter(
            task_template_id__in=task_template_ids)
        _validate_task_stage_objs(task_stages, task_template_stages_dtos)
