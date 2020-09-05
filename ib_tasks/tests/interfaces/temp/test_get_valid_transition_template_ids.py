import pytest

from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ib_tasks.tests.factories.models import \
    TaskTemplateWithTransitionFactory, \
    TaskTemplateFactory


@pytest.mark.django_db
class TestGetValidTaskTemplateIds:

    @pytest.fixture()
    def populate_data(self):
        TaskTemplateFactory.reset_sequence()
        TaskTemplateWithTransitionFactory.create_batch(size=6)

    def test_get_valid_task_template_ids_given_ids(self, populate_data):
        # Arrange
        expected_response = ["template_1", "template_3",
                             "template_5"]
        transition_template_ids = ["template_2", "template_4",
                                   "template_6", "template_1", "template_3",
                                   "template_5"]
        storage = TaskTemplateStorageImplementation()

        # Act
        response = storage.get_valid_transition_template_ids(transition_template_ids)

        # Assert
        assert response == expected_response

    def test_get_valid_task_template_ids_given_ids_are_invalid(self, populate_data):
        # Arrange
        expected_response = []
        transition_template_ids = ["template_2", "template_4",
                                   "template_6"]
        storage = TaskTemplateStorageImplementation()

        # Act
        response = storage.get_valid_transition_template_ids(transition_template_ids)

        # Assert
        assert response == expected_response
