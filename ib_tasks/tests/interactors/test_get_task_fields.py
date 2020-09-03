from unittest.mock import create_autospec

import pytest

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.get_task_fields import GetTaskFieldsInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDetailsDTOWithTaskId
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_projects_mock
from ib_tasks.tests.factories.storage_dtos import (
    FieldDetailsDTOWithTaskIdFactory)


class TestGetFieldsAndActionsInteractor:

    @pytest.fixture
    def field_storage_mock(self):
        return create_autospec(FieldsStorageInterface)

    @pytest.fixture()
    def get_fields_dtos(self):
        FieldDetailsDTOWithTaskIdFactory.reset_sequence()
        fields = FieldDetailsDTOWithTaskIdFactory.create_batch(size=2,
                                                               task_id=1)
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        fields.append(FieldDetailsDTOWithTaskIdFactory(task_id=2))
        return fields

    @pytest.fixture
    def expected_output(self):
        return [
            FieldDetailsDTOWithTaskId(
                field_type='Drop down', field_id='FIELD-ID-1', key='key', value='value',
                task_id=1),
            FieldDetailsDTOWithTaskId(
                field_type='Drop down', field_id='FIELD-ID-2', key='key', value='value',
                task_id=1),
            FieldDetailsDTOWithTaskId(
                field_type='Drop down', field_id='FIELD-ID-3', key='key', value='value',
                task_id=2),
            FieldDetailsDTOWithTaskId(
                field_type='Drop down', field_id='FIELD-ID-4', key='key', value='value',
                task_id=2)]

    def test_get_fields_given_task_stage_details(self,
                                                 mocker,
                                                 field_storage_mock,
                                                 get_fields_dtos,
                                                 expected_output,
                                                 get_task_template_stage_dtos):
        # Arrange
        view_type = ViewType.KANBAN.value
        field_dtos = get_fields_dtos
        user_id = "user_id_1"
        task_project_dtos = [TaskProjectDTO(project_id="project_id_1",
                                            task_id=1),
                             TaskProjectDTO(project_id="project_id_1",
                                            task_id=2)]
        user_roles = [ProjectRolesDTO(
            project_id="project_id_1",
            roles=["FIN_PAYMENT_REQUESTER",
                   "FIN_PAYMENT_POC",
                   "FIN_PAYMENT_APPROVER",
                   "FIN_PAYMENTS_RP",
                   "FIN_FINANCE_RP"])]
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        field_storage_mock.get_fields_details.return_value = field_dtos
        interactor = GetTaskFieldsInteractor(field_storage_mock)

        # Act
        response = interactor.get_task_fields(task_stage_dtos=get_task_template_stage_dtos,
                                              view_type=view_type,
                                              user_id=user_id,
                                              task_project_dtos=task_project_dtos)

        # Assert
        assert response == expected_output
