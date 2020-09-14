import pytest

from ib_tasks.models import TaskTemplateInitialStage
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import TemplateStageDTOFactory
from ib_tasks.tests.factories.models import (TaskTemplateWithTransitionFactory,
                                             StageModelFactory,
                                             TaskTemplateFactory)


@pytest.mark.django_db
class TestCreateInitialStageToTemplate:
    @pytest.fixture
    def populate_data(self):
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence(1)
        StageModelFactory.create_batch(4)
        TaskTemplateWithTransitionFactory.create_batch(4)

    @pytest.fixture
    def expected_output(self):
        TemplateStageDTOFactory.reset_sequence(1)
        return TemplateStageDTOFactory.create_batch(4)

    @staticmethod
    def _validate_template_stages(expected_output, returned_output):
        for expected, returned in zip(expected_output, returned_output):
            assert expected.task_template_id == \
                   returned.task_template_id
            assert expected.stage_id == returned.stage.stage_id

    def test_given_valid_details_populate_data(self, populate_data,
                                               expected_output):
        # Arrange
        data = expected_output
        stage_ids = [item.stage_id for item in data]
        storage = ActionsStorageImplementation()

        # Act
        storage.create_initial_stage_to_task_template(data)

        # Assert
        objs = TaskTemplateInitialStage.objects.filter(
                stage__stage_id__in=stage_ids)
        self._validate_template_stages(expected_output, objs)
