import pytest



@pytest.mark.django_db
class TestGetEnableMultipleGofIds:

    def test_given_valid_details_returns_multiple_enable_gof_ids(self):

        # Arrange
        task_id = 1

        from ib_tasks.storages.storage_implementation \
            import StorageImplementation

        from ib_tasks.tests.factories.models import (
            TaskTemplateFactory, TaskModelFactory,
            GoFToTaskTemplateFactory, GoFFactory
        )
        GoFFactory.reset_sequence(0)
        TaskTemplateFactory.reset_sequence(0)
        TaskModelFactory.reset_sequence(0)
        GoFToTaskTemplateFactory.reset_sequence(0)
        TaskModelFactory()
        task_template = TaskTemplateFactory()
        GoFToTaskTemplateFactory.create_batch(
            size=2, task_template=task_template,
            enable_add_another_gof=True
        )
        GoFToTaskTemplateFactory(
            task_template=task_template,
            enable_add_another_gof=False
        )
        from ib_tasks.tests.factories.storage_dtos \
            import GOFMultipleEnableDTOFactory
        storage = StorageImplementation()
        GOFMultipleEnableDTOFactory.reset_sequence(1)
        expected = GOFMultipleEnableDTOFactory.create_batch(size=2)
        expected.append(GOFMultipleEnableDTOFactory(multiple_status=False))
        gof_ids = ['gof_1', 'gof_2', 'gof_3']
        template_id = "template_1"

        # Act
        response = storage.get_enable_multiple_gofs_field_to_gof_ids(
            template_id=template_id, gof_ids=gof_ids
        )

        # Assert
        assert response == expected
