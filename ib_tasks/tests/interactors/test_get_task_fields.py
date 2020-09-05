from unittest.mock import create_autospec

import pytest

from ib_tasks.adapters.dtos import ProjectRolesDTO
from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.get_task_fields import GetTaskFieldsInteractor
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    (FieldDetailsDTOWithTaskId, TaskTemplateStageFieldsDTO)
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_projects_mock
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_get_field_ids_having_permission_for_user_projects
from ib_tasks.tests.factories.interactor_dtos import GetTaskDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import (
    FieldDetailsDTOWithTaskIdFactory, TaskTemplateStagesDTOFactory)


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
    def task_storage_mock(self):
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def expected_output(self):
        fields = [
                FieldDetailsDTOWithTaskId(
                        field_type='Drop down', field_id='FIELD-ID-1',
                        key='key', value='value',
                        task_id=1),
                FieldDetailsDTOWithTaskId(
                        field_type='Drop down', field_id='FIELD-ID-2',
                        key='key', value='value',
                        task_id=1),
                FieldDetailsDTOWithTaskId(
                        field_type='Drop down', field_id='FIELD-ID-3',
                        key='key', value='value',
                        task_id=2),
                FieldDetailsDTOWithTaskId(
                        field_type='Drop down', field_id='FIELD-ID-4',
                        key='key', value='value',
                        task_id=2)]
        stage_fields_dtos = [TaskTemplateStageFieldsDTO(
                task_template_id='task_template_id_1', task_id=1,
                stage_id='stage_id_1', display_name='display_name_1',
                db_stage_id=1, stage_color='blue',
                field_ids=['FIELD-ID-1', 'FIELD-ID-2']),
                TaskTemplateStageFieldsDTO(
                        task_template_id='task_template_id_1',
                        task_id=1, stage_id='stage_id_2',
                        display_name='display_name_2',
                        db_stage_id=2, stage_color='blue',
                        field_ids=['FIELD-ID-3', 'FIELD-ID-4'])]
        return fields, stage_fields_dtos

    @pytest.fixture()
    def get_field_ids(self):
        return [TaskTemplateStageFieldsDTO(
                task_template_id="task_template_id_1",
                task_id=1,
                db_stage_id=1,
                stage_color="blue",
                display_name="display_name_1",
                stage_id="stage_id_1",
                field_ids=["FIELD-ID-1", "FIELD-ID-2"]
        ),
                TaskTemplateStageFieldsDTO(
                        task_template_id="task_template_id_1",
                        task_id=1,
                        db_stage_id=2,
                        stage_color="blue",
                        display_name="display_name_2",
                        stage_id="stage_id_2",
                        field_ids=["FIELD-ID-3", "FIELD-ID-4"]
                )
        ]

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(
                size=2, task_template_id="task_template_id_1")

    @pytest.fixture()
    def get_task_dtos(self):
        GetTaskDetailsDTOFactory.reset_sequence()
        return GetTaskDetailsDTOFactory.create_batch(size=2, task_id=1)

    @pytest.fixture()
    def get_task_template_stage_dtos_for_two_stages(self):
        TaskTemplateStagesDTOFactory.reset_sequence()
        return TaskTemplateStagesDTOFactory.create_batch(
                size=2, task_template_id="task_template_id_1", task_id=1)

    def test_get_fields_given_task_stage_details(self,
                                                 mocker,
                                                 field_storage_mock,
                                                 get_fields_dtos,
                                                 get_field_ids,
                                                 task_storage_mock,
                                                 expected_output,
                                                 get_task_dtos,
                                                 get_task_template_stage_dtos):
        # Arrange
        view_type = ViewType.KANBAN.value
        field_dtos = get_fields_dtos
        user_id = "user_id_1"
        task_ids = [1, 2]
        user_roles = [ProjectRolesDTO(
                project_id="project_id_1",
                roles=["FIN_PAYMENT_REQUESTER",
                       "FIN_PAYMENT_POC",
                       "FIN_PAYMENT_APPROVER",
                       "FIN_PAYMENTS_RP",
                       "FIN_FINANCE_RP"])]
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        field_ids = ['FIELD-ID-1', 'FIELD-ID-2', 'FIELD-ID-3', 'FIELD-ID-4']
        field_storage_mock.get_field_ids.return_value = get_field_ids
        task_storage_mock.get_valid_task_ids.return_value = task_ids
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        field_storage_mock.get_fields_details.return_value = field_dtos
        interactor = GetTaskFieldsInteractor(field_storage_mock,
                                             task_storage_mock
                                             )

        # Act
        response = interactor.get_task_fields(
                task_stage_dtos=get_task_template_stage_dtos,
                view_type=view_type,
                user_id=user_id,
                task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)
        field_storage_mock.get_field_ids.assert_called_once_with(
                get_task_template_stage_dtos, view_type)
        assert response == expected_output

    def test_get_fields_given_task_is_in_two_stages(self,
                                                    mocker,
                                                    field_storage_mock,
                                                    get_fields_dtos,
                                                    get_field_ids,
                                                    task_storage_mock,
                                                    get_task_dtos,
                                                    expected_output,
                                                    get_task_template_stage_dtos):
        # Arrange
        view_type = ViewType.KANBAN.value
        field_dtos = get_fields_dtos
        user_id = "user_id_1"
        task_ids = [1, 2]
        user_roles = [ProjectRolesDTO(
                project_id="project_id_1",
                roles=["FIN_PAYMENT_REQUESTER",
                       "FIN_PAYMENT_POC",
                       "FIN_PAYMENT_APPROVER",
                       "FIN_PAYMENTS_RP",
                       "FIN_FINANCE_RP"])]
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        field_ids = ['FIELD-ID-1', 'FIELD-ID-2', 'FIELD-ID-3', 'FIELD-ID-4']
        field_storage_mock.get_field_ids.return_value = get_field_ids
        task_storage_mock.get_valid_task_ids.return_value = task_ids
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        field_storage_mock.get_fields_details.return_value = field_dtos
        interactor = GetTaskFieldsInteractor(field_storage_mock,
                                             task_storage_mock
                                             )

        # Act
        response = interactor.get_task_fields(
                task_stage_dtos=get_task_template_stage_dtos,
                view_type=view_type,
                user_id=user_id,
                task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)
        field_storage_mock.get_field_ids.assert_called_once_with(
                get_task_template_stage_dtos, view_type)
        assert response == expected_output

    def test_get_fields_when_invalid_task_id_raises_exception(
            self,
            mocker,
            field_storage_mock,
            get_fields_dtos,
            get_field_ids,
            task_storage_mock,
            get_task_dtos,
            expected_output,
            get_task_template_stage_dtos):
        # Arrange
        view_type = ViewType.KANBAN.value
        field_dtos = get_fields_dtos
        user_id = "user_id_1"
        task_ids = [1, 2]
        user_roles = [ProjectRolesDTO(
                project_id="project_id_1",
                roles=["FIN_PAYMENT_REQUESTER",
                       "FIN_PAYMENT_POC",
                       "FIN_PAYMENT_APPROVER",
                       "FIN_PAYMENTS_RP",
                       "FIN_FINANCE_RP"])]
        user_roles_mock = get_user_role_ids_based_on_projects_mock(mocker)
        user_roles_mock.return_value = user_roles
        field_ids = ['FIELD-ID-1', 'FIELD-ID-2', 'FIELD-ID-3', 'FIELD-ID-4']
        task_storage_mock.get_valid_task_ids.return_value = [1]
        prepare_get_field_ids_having_permission_for_user_projects(mocker,
                                                                  field_ids)
        field_storage_mock.get_fields_details.return_value = field_dtos
        interactor = GetTaskFieldsInteractor(field_storage_mock,
                                             task_storage_mock
                                             )

        # Act
        with pytest.raises(InvalidTaskIds) as err:
            interactor.get_task_fields(
                task_stage_dtos=get_task_template_stage_dtos,
                view_type=view_type,
                user_id=user_id,
                task_ids=task_ids)

        # Assert
        task_storage_mock.get_valid_task_ids.assert_called_once_with(task_ids)
