import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import (
    StageModelFactory, TaskFactory, TaskTemplateFactory, TaskStageModelFactory, FieldFactory, TaskGoFFieldFactory,
    TaskGoFFactory)
from ib_tasks.tests.factories.storage_dtos import TaskFieldsDTOFactory


@pytest.mark.django_db
class TestGetFieldDetails:

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskFieldsDTOFactory.reset_sequence()
        return TaskFieldsDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        TaskFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        TaskGoFFieldFactory.create_batch(size=4)

    def test_get_field_details(self, get_task_template_stage_dtos,
                               populate_data,
                               snapshot):
        # Arrange
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_fields_details(get_task_template_stage_dtos)

        # Assert
        snapshot.assert_match(response, "response")
