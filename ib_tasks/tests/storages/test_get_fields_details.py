import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import (
    StageModelFactory, TaskFactory, TaskTemplateFactory, TaskStageModelFactory, FieldFactory, TaskGoFFieldFactory,
    TaskGoFFactory, GoFFactory, FieldRoleFactory)
from ib_tasks.tests.factories.storage_dtos import TaskFieldsDTOFactory, TaskWithFieldsDTOFactory


@pytest.mark.django_db
class TestGetFieldDetails:

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskWithFieldsDTOFactory.reset_sequence()
        tasks = [TaskWithFieldsDTOFactory(), TaskWithFieldsDTOFactory(
            field_ids=["FIELD_ID-0", "FIELD_ID-1", "FIELD_ID-2"])]
        return tasks

    @pytest.fixture()
    def populate_data(self):
        GoFFactory.reset_sequence(-1)
        GoFFactory.create_batch(size=4)
        TaskFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=4)
        fields = FieldFactory.create_batch(size=4)
        TaskGoFFieldFactory(field=fields[0], task_gof__task_id=2)
        TaskGoFFieldFactory(field=fields[1], task_gof__task_id=1)
        TaskGoFFieldFactory(field=fields[2], task_gof__task_id=2)
        TaskGoFFieldFactory(field=fields[2], task_gof__task_id=1)
        TaskGoFFieldFactory(field=fields[1], task_gof__task_id=2)
        FieldRoleFactory(field=fields[0])
        FieldRoleFactory(field=fields[0])
        FieldRoleFactory(field=fields[1])
        FieldRoleFactory(field=fields[1])
        FieldRoleFactory(field=fields[2])
        FieldRoleFactory(field=fields[2])

    def test_when_user_permitted_fields_exists_returns_field_details(
            self, get_task_template_stage_dtos,
            populate_data,
            snapshot):
        # Arrange
        user_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_fields_details(get_task_template_stage_dtos,
                                              user_roles)

        # Assert
        snapshot.assert_match(response, "response")

    def test_when_user_donot_have_permissions_for_fields(
            self, get_task_template_stage_dtos,
            populate_data,
            snapshot):
        # Arrange
        user_roles = ["role_1", "role_2", "role_3"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_fields_details(get_task_template_stage_dtos,
                                              user_roles)

        # Assert
        snapshot.assert_match(response, "response")
