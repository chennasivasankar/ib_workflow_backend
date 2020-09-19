import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestGetStageIdWithTemplateIdDTOs:

    def test_when_stages_for_task_templates_exists_returns_dtos(
            self, snapshot):
        # Arrange
        task_template_ids = ["template_1", "template_2"]

        import factory
        from ib_tasks.tests.factories.models import StageModelFactory, \
            TaskTemplateFactory
        StageModelFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()

        TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(task_template_ids))
        StageModelFactory.create_batch(
            size=4, task_template_id=factory.Iterator(task_template_ids))

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_id_with_template_id_dtos(
            task_template_ids=task_template_ids)

        # Assert
        snapshot.assert_match(response, "stage_id_with_template_id_dtos")

    def test_when_no_stages_for_task_templates_exists_returns_empty_list(
            self, snapshot):
        # Arrange
        task_template_ids = ["template_1", "template_2"]
        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_id_with_template_id_dtos(
            task_template_ids=task_template_ids)

        # Assert
        snapshot.assert_match(response, "stage_id_with_template_id_dtos")
