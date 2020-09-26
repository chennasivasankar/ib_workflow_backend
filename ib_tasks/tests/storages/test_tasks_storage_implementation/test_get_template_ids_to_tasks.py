import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestCheckIsTaskExists:

    def expected(self):
        from ib_tasks.tests.factories.storage_dtos import TaskTemplateMapDTOFactory
        TaskTemplateMapDTOFactory.reset_sequence(1)
        response = [TaskTemplateMapDTOFactory()]
        return response

    def test_given_valid_task_ids_returns_task_template_dtos(self, storage):
        # Arrange
        TaskFactory.reset_sequence(1)
        TaskFactory()
        task_id = 1
        expected = self.expected()

        # Act
        response = storage.get_template_ids_to_task_ids(task_ids=[task_id])

        # Assert
        assert response == expected
