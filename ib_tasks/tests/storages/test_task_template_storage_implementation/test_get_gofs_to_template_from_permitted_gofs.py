import pytest


@pytest.mark.django_db
class TestGetGoFsToTemplateFromPermittedGoFs:

    def test_get_gofs_to_template_from_permitted_gofs(self, storage):
        # Arrange
        import factory
        from ib_tasks.tests.factories.models import \
            GoFToTaskTemplateFactory, GoFFactory
        from ib_tasks.tests.factories.storage_dtos import \
            GoFToTaskTemplateDTOFactory
        template_id = "template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        expected_gof_to_task_templates_dtos = \
            GoFToTaskTemplateDTOFactory.create_batch(
                size=2, gof_id=factory.Iterator(expected_gof_ids),
                template_id=template_id
            )

        gof_objects = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids),
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_objects),
            task_template_id=template_id
        )

        # Act
        result = storage.get_gofs_to_template_from_permitted_gofs(
            gof_ids=expected_gof_ids, template_id=template_id
        )

        # Assert
        assert result == expected_gof_to_task_templates_dtos
