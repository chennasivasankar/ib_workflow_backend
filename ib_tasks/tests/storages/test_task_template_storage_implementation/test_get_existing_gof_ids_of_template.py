import pytest


@pytest.mark.django_db
class TestGetExistingGoFIdsOfTemplate:

    def test_get_existing_gof_ids_of_template(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import \
            TaskTemplateWith2GoFsFactory

        template_id = "FIN_VENDOR"
        expected_gof_ids = ['gof_1', 'gof_2']
        TaskTemplateWith2GoFsFactory(template_id=template_id)

        # Act
        existing_gof_ids_of_template = \
            storage.get_existing_gof_ids_of_template(template_id=template_id)

        # Assert
        assert existing_gof_ids_of_template == expected_gof_ids
