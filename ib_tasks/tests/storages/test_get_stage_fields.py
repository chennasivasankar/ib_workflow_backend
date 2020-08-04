import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import (
    StageModelFactory, TaskFactory, TaskTemplateFactory, TaskStageModelFactory)
from ib_tasks.tests.factories.storage_dtos import TemplateStagesDTOFactory


@pytest.mark.django_db
class TestGetFieldIds:

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TemplateStagesDTOFactory.reset_sequence()
        return TemplateStagesDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.create_batch(size=3)
        TaskStageModelFactory.reset_sequence()
        TaskStageModelFactory.create_batch(size=4)

    def test_get_field_ids(self, get_task_template_stage_dtos,
                           populate_data,
                           snapshot):
        # Arrange
        user_roles = ["FIN_PAYMENT_REQUESTER",
                      "FIN_PAYMENT_POC",
                      "FIN_PAYMENT_APPROVER",
                      "FIN_PAYMENTS_RP",
                      "FIN_FINANCE_RP"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_field_ids(get_task_template_stage_dtos,
                                         user_roles=user_roles)

        # Assert
        snapshot.assert_match(response, "response")
