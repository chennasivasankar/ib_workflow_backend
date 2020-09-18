import pytest


@pytest.mark.django_db
class TestGetGoFIdsForGiventemplate:

    def test_get_gof_ids_for_given_template(self):
        # Arrange
        from ib_tasks.tests.factories.models import GoFToTaskTemplateFactory
        from ib_tasks.tests.factories.models import TaskTemplateFactory
        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        template_obj = TaskTemplateFactory()
        task_template_gofs = GoFToTaskTemplateFactory.create_batch(
            size=5, task_template=template_obj
        )
        expected_gof_ids = [
            task_template_gof.gof_id
            for task_template_gof in task_template_gofs
        ]
        template_id = template_obj.template_id
        storage = GoFStorageImplementation()

        # Act
        actual_gof_ids = storage.get_gof_ids_for_given_template(template_id)

        # Assert
        assert expected_gof_ids == actual_gof_ids