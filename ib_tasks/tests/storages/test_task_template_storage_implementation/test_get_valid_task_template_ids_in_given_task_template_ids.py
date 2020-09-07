import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory


@pytest.mark.django_db
class TestGetValidTaskTemplateIdsInGivenTaskTemplateIds:

    def test_get_valid_template_ids_in_given_template_ids(self, storage):
        # Arrange
        task_template = TaskTemplateFactory()
        template_ids = [task_template.template_id, "FIN_VENDOR"]
        expected_valid_template_ids = [task_template.template_id]

        # Act
        actual_valid_template_ids = \
            storage.get_valid_task_template_ids_in_given_task_template_ids(
                template_ids)

        # Assert
        assert expected_valid_template_ids == actual_valid_template_ids
