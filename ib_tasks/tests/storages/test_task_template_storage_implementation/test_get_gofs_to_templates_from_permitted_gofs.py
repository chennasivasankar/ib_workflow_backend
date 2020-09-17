import pytest


@pytest.mark.django_db
class TestGetGoFsToTemplatesFromPermittedGoFs:

    def test_get_gofs_to_templates_from_permitted_gofs(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import \
            GoFToTaskTemplateFactory, GoFFactory
        from ib_tasks.interactors.storage_interfaces.gof_dtos import \
            GoFToTaskTemplateDTO
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_gof_to_task_templates_dtos = [
            GoFToTaskTemplateDTO(gof_id='gof_1', template_id='template_1',
                                 order=0, enable_add_another=True),
            GoFToTaskTemplateDTO(gof_id='gof_2', template_id='template_2',
                                 order=1, enable_add_another=False)]

        import factory
        gof_objects = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids)
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_objects)
        )

        # Act
        result = storage.get_gofs_to_templates_from_given_gofs(
            gof_ids=expected_gof_ids
        )

        # Assert
        assert result == expected_gof_to_task_templates_dtos
