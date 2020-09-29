import pytest


class TestGetMaxStageValueForGivenTemplateId:

    @pytest.mark.django_db
    def test_given_template_id_return_max_stage_value(self):
        # Arrange
        task_template_id = "Adhoc template"
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(
            size=4, task_template_id=task_template_id
        )
        from ib_tasks.storages.task_stage_storage_implementation import \
            TaskStageStorageImplementation
        storage = TaskStageStorageImplementation()
        max_stage_value = 3

        # Act
        actual_max_stage_value = \
            storage.get_max_stage_value_for_the_given_template(
                task_template_id)

        # Assert
        assert max_stage_value == actual_max_stage_value
