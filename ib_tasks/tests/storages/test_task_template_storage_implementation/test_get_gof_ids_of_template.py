import pytest


@pytest.mark.django_db
class TestGetGoFIdsOfTemplate:

    def test_get_gof_ids_of_template_when_exists_returns_gof_ids(
            self, storage):
        # Arrange
        import factory
        from ib_tasks.tests.factories.models import \
            GoFToTaskTemplateFactory, GoFFactory

        template_id = "template_1"
        expected_gof_ids = ['gof_1', 'gof_2']
        gof_objects = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(expected_gof_ids),
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_objects),
            task_template_id=template_id
        )

        # Act
        result = storage.get_gof_ids_of_template(template_id=template_id)

        # Assert
        assert result == expected_gof_ids

    def test_get_gof_ids_of_template_when_not_exists_returns_empty_list(
            self, storage):
        # Arrange
        template_id = "template_1"
        expected_gof_ids = []
        # Act
        result = storage.get_gof_ids_of_template(template_id=template_id)

        # Assert
        assert result == expected_gof_ids
