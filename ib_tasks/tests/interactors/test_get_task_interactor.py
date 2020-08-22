from unittest.mock import create_autospec, patch

import factory
import pytest

from ib_tasks.adapters.searchable_details_service import \
    SearchableDetailsService, InvalidUserIdsException, \
    InvalidStateIdsException, InvalidCountryIdsException, \
    InvalidCityIdsException
from ib_tasks.constants.enum import ValidationType, Searchable
from ib_tasks.interactors.get_stages_assignees_details_interactor import \
    GetStagesAssigneesDetailsInteractor
from ib_tasks.interactors.get_task_base_interactor \
    import GetTaskBaseInteractor
from ib_tasks.interactors.get_task_interactor \
    import GetTaskInteractor
from ib_tasks.interactors.get_task_stages_and_actions \
    import GetTaskStagesAndActions
from ib_tasks.tests.factories.storage_dtos import \
    StageActionDetailsDTOFactory, \
    FieldSearchableDTOFactory


class TestGetTaskInteractor:

    @pytest.fixture
    def task_crud_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        task_crud_storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return task_crud_storage

    @pytest.fixture
    def stages_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface \
            import FieldsStorageInterface
        stages_storage_mock = create_autospec(FieldsStorageInterface)
        return stages_storage_mock

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        storage = create_autospec(ActionStorageInterface)
        return storage

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        storage = create_autospec(TaskStageStorageInterface)
        return storage

    @pytest.fixture
    def reset_sequence(self):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskStageAssigneeDTOFactory
        TaskStageAssigneeDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.adapter_dtos import \
            AssigneeDetailsDTOFactory
        AssigneeDetailsDTOFactory.reset_sequence()

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces \
            .get_task_presenter_interface \
            import GetTaskPresenterInterface
        presenter = create_autospec(GetTaskPresenterInterface)
        return presenter

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

    @pytest.fixture
    def task_gof_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFDTOFactory
        task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=2, gof_id="gof2", same_gof_order=0)
        ]
        return task_gof_dtos

    @pytest.fixture
    def gof_ids(self):
        gof_ids = ["gof0", "gof1", "gof2"]
        return gof_ids

    @pytest.fixture
    def permission_gof_ids(self):
        permission_gof_ids = ["gof0", "gof1"]
        return permission_gof_ids

    @pytest.fixture
    def permission_task_gof_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFDTOFactory
        permission_task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
        ]
        return permission_task_gof_dtos

    @pytest.fixture
    def task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field1",
                                   field_response="response1"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3"),
            TaskGoFFieldDTOFactory(task_gof_id=2, field_id="field4",
                                   field_response="response4")
        ]
        return task_gof_field_dtos

    @pytest.fixture
    def task_base_details_dto(self):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskBaseDetailsDTOFactory
        task_base_details_dto = TaskBaseDetailsDTOFactory()
        return task_base_details_dto

    @pytest.fixture
    def field_ids(self):
        field_ids = ["field0", "field1", "field2", "field3"]
        return field_ids

    @pytest.fixture
    def permission_field_ids(self):
        permission_field_ids = ["field0", "field2", "field3"]
        return permission_field_ids

    @pytest.fixture
    def permission_task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        permission_task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3")
        ]
        return permission_task_gof_field_dtos

    @pytest.fixture
    def task_details_dto(
            self, task_gof_dtos, task_gof_field_dtos, task_base_details_dto
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos=task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def permission_task_details_dto(
            self, permission_task_gof_dtos, permission_task_gof_field_dtos,
            task_base_details_dto
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=permission_task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def user_roles(self):
        user_role_ids = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER',
                         'FIN_PAYMENT_POC',
                         'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                         'FIN_COMPLIANCE_APPROVER',
                         'FIN_PAYMENTS_LEVEL1_VERIFIER',
                         'FIN_PAYMENTS_LEVEL2_VERIFIER',
                         'FIN_PAYMENTS_LEVEL3_VERIFIER',
                         'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                         'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                         'FIN_ACCOUNTS_LEVEL2_VERIFIER']
        return user_role_ids

    @pytest.fixture
    def stages_action_dtos(self):
        stages_action_dtos = [
            StageActionDetailsDTOFactory(
                stage_id="stage0",
                action_type=ValidationType.NO_VALIDATIONS.value
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage0",
                action_type=None
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage1",
                action_type=ValidationType.NO_VALIDATIONS.value
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage1",
                action_type=None
            ),
        ]
        return stages_action_dtos

    @pytest.fixture
    def stages_and_actions_details_dtos(self, stages_action_dtos):
        from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO
        stages_and_actions_details_dtos = [
            StageAndActionsDetailsDTO(
                stage_id="stage0",
                name="name1",
                db_stage_id=1,
                color="color1",
                actions_dtos=[stages_action_dtos[0], stages_action_dtos[1]]
            ),
            StageAndActionsDetailsDTO(
                stage_id="stage1",
                name="name2",
                db_stage_id=1,
                color="color2",
                actions_dtos=[stages_action_dtos[2], stages_action_dtos[3]]
            )
        ]
        return stages_and_actions_details_dtos

    @pytest.fixture
    def assignee_details_dtos(self):
        from ib_tasks.tests.factories.adapter_dtos import \
            AssigneeDetailsDTOFactory
        assignee_details_dtos = [
            AssigneeDetailsDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174001"),
            AssigneeDetailsDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174002"),
            AssigneeDetailsDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174003")
        ]
        return assignee_details_dtos

    @pytest.fixture
    def stage_assignee_dtos(self):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskStageAssigneeDTOFactory
        stage_assignee_dtos = [
            TaskStageAssigneeDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174001"),
            TaskStageAssigneeDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174002"),
            TaskStageAssigneeDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174003"),
            TaskStageAssigneeDTOFactory(assignee_id=None)
        ]
        return stage_assignee_dtos

    @pytest.fixture
    def stage_assignee_details_dtos(
            self, assignee_details_dtos, stage_assignee_dtos
    ):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDetailsDTOFactory
        stage_assignee_details_dtos = [
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[0].task_stage_id,
                stage_id=stage_assignee_dtos[0].stage_id,
                assignee_details_dto=assignee_details_dtos[0]),
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[1].task_stage_id,
                stage_id=stage_assignee_dtos[1].stage_id,
                assignee_details_dto=assignee_details_dtos[1]),
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[2].task_stage_id,
                stage_id=stage_assignee_dtos[2].stage_id,
                assignee_details_dto=assignee_details_dtos[2]),
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[3].task_stage_id,
                stage_id=stage_assignee_dtos[3].stage_id,
                assignee_details_dto=None)
        ]
        return stage_assignee_details_dtos

    @pytest.fixture
    def task_complete_details_dto(
            self, permission_task_details_dto,
            stages_and_actions_details_dtos,
            stage_assignee_details_dtos
    ):
        from ib_tasks.interactors.presenter_interfaces \
            .get_task_presenter_interface \
            import TaskCompleteDetailsDTO
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_details_dto=permission_task_details_dto,
            stages_and_actions_details_dtos=stages_and_actions_details_dtos,
            stage_assignee_details_dtos=stage_assignee_details_dtos
        )
        return task_complete_details_dto

    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_invalid_task_id_raise_exception(
            self, get_task_mock, presenter_mock,
            mock_object, task_crud_storage_mock,
            stages_storage_mock, storage_mock,
            task_storage_mock, action_storage_mock,
            task_stage_storage_mock, reset_sequence
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        user_id = "user1"
        task_display_id = "IBWF-1"
        task_id = 1
        exception_object = InvalidTaskIdException(task_id)
        get_task_mock.side_effect = exception_object
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_task_id.return_value = \
            mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_exception_for_invalid_task_id. \
            assert_called_once_with(exception_object)

    def test_given_invalid_task_display_id_raise_exception(
            self, presenter_mock,
            mock_object, task_crud_storage_mock,
            stages_storage_mock, storage_mock,
            task_storage_mock, action_storage_mock,
            task_stage_storage_mock, reset_sequence
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId
        user_id = "user1"
        task_display_id = "IBWF-1"
        exception_object = InvalidTaskDisplayId(task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        presenter_mock.raise_invalid_task_display_id.return_value = \
            mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        call_tuple = presenter_mock.raise_invalid_task_display_id.call_args
        error_obj = call_tuple.args[0]
        assert error_obj.task_display_id == exception_object.task_display_id

    @patch.object(GetTaskStagesAndActions, "get_task_stages_and_actions")
    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_and_valid_stage_ids_but_user_has_no_permission_raise_exception(
            self, get_task_mock,
            get_task_stages_and_actions_mock, stage_assignee_details_dtos,
            mocker, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_details_dto, user_roles, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            permission_task_gof_field_dtos, mock_object,
            stages_and_actions_details_dtos, permission_gof_ids,
            reset_sequence,
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = task_details_dto
        get_task_stages_and_actions_mock.return_value = \
            stages_and_actions_details_dtos
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = False
        task_crud_storage_mock.get_field_searchable_dtos.return_value = []

        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        presenter_mock.raise_user_permission_denied.return_value = mock_object

        # Act
        response = interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )
        # Assert
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles
        )
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(
            field_ids, user_roles)
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.assert_called_once()
        presenter_mock.raise_user_permission_denied.assert_called_once()
        assert response == mock_object

    @patch.object(GetTaskStagesAndActions, "get_task_stages_and_actions")
    @patch.object(GetTaskBaseInteractor, 'get_task')
    @patch.object(GetStagesAssigneesDetailsInteractor,
                  "get_stages_assignee_details_dtos")
    def test_given_valid_task_and_invalid_stage_ids_raise_exception(
            self, stage_assignee_details_dtos_mock, get_task_mock,
            get_task_stages_and_actions_mock, stage_assignee_details_dtos,
            mocker, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_details_dto, user_roles, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            permission_task_gof_field_dtos, task_complete_details_dto,
            mock_object, stages_and_actions_details_dtos, permission_gof_ids,
            reset_sequence,
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStageIdsForTask
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS_FOR_TASK
        invalid_stages_ids = [1, 2, 3]
        message = INVALID_STAGE_IDS_FOR_TASK.format(
            invalid_stages_ids, task_id
        )
        exception_object = InvalidStageIdsForTask(message)
        get_task_mock.return_value = task_details_dto
        stage_assignee_details_dtos_mock.side_effect = \
            exception_object
        get_task_stages_and_actions_mock.return_value = \
            stages_and_actions_details_dtos
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        task_crud_storage_mock.get_field_searchable_dtos.return_value = []

        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        presenter_mock.raise_invalid_stage_ids_for_task.return_value = \
            mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )
        # Assert
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles
        )
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(
            field_ids, user_roles)
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.assert_called_once()
        presenter_mock.raise_invalid_stage_ids_for_task.assert_called_once()

    @patch.object(GetTaskStagesAndActions, "get_task_stages_and_actions")
    @patch.object(GetTaskBaseInteractor, 'get_task')
    @patch.object(GetStagesAssigneesDetailsInteractor,
                  "get_stages_assignee_details_dtos")
    def test_given_valid_task_returns_task_complete_details_dto(
            self, stage_assignee_details_dtos_mock, get_task_mock,
            get_task_stages_and_actions_mock, stage_assignee_details_dtos,
            mocker, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_details_dto, user_roles, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            permission_task_gof_field_dtos, task_complete_details_dto,
            mock_object, stages_and_actions_details_dtos, permission_gof_ids,
            reset_sequence,
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = task_details_dto
        stage_assignee_details_dtos_mock.return_value = \
            stage_assignee_details_dtos
        get_task_stages_and_actions_mock.return_value = \
            stages_and_actions_details_dtos
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        task_crud_storage_mock.get_field_searchable_dtos.return_value = []

        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        presenter_mock.get_task_response.return_value = mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )
        # Assert
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(
            field_ids, user_roles)
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.assert_called_once()
        presenter_mock.get_task_response.assert_called_once_with(
            task_complete_details_dto)

    @pytest.fixture
    def field_searchable_dtos(self):
        field_searchable_dtos = [
            FieldSearchableDTOFactory(
                field_id="field0",
                field_value=Searchable.CITY.value,
                field_response="1"
            ),
            FieldSearchableDTOFactory(
                field_id="field2",
                field_value=Searchable.USER.value,
                field_response="123e4567-e89b-12d3-a456-426614174000"
            )
        ]
        return field_searchable_dtos

    @pytest.fixture
    def field_searchable_dtos_with_invalid_city_ids(self):
        field_searchable_dtos = [
            FieldSearchableDTOFactory(
                field_id="field0",
                field_value=Searchable.CITY.value,
                field_response="100"
            ),
            FieldSearchableDTOFactory(
                field_id="field2",
                field_value=Searchable.CITY.value,
                field_response="110"
            )
        ]
        return field_searchable_dtos

    @pytest.fixture
    def task_gof_field_dtos_with_searchable_field_type(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response="1"),
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field1",
                                   field_response="response1"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response="123e4567-e89b-12d3-a456-426614174000"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3"),
            TaskGoFFieldDTOFactory(task_gof_id=2, field_id="field4",
                                   field_response="response4")
        ]
        return task_gof_field_dtos

    @pytest.fixture
    def permission_task_gof_field_dtos_with_field_type_searchable(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        permission_task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response='{"id": 1, "value": '
                                                  '"Hyderabad"}'),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response='{"id": '
                                                  '"123e4567-e89b-12d3-a456-426614174000", "value": "User1"}'),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3")
        ]
        return permission_task_gof_field_dtos

    @pytest.fixture
    def task_details_dto_with_some_fields_searchable_type(
            self, task_gof_dtos,
            task_base_details_dto,
            task_gof_field_dtos_with_searchable_field_type
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=task_gof_dtos,
            task_gof_field_dtos
            =task_gof_field_dtos_with_searchable_field_type
        )
        return task_details_dto

    @pytest.fixture
    def permission_task_details_dto_with_fields_searchable_type(
            self, permission_task_gof_dtos,
            task_base_details_dto,
            permission_task_gof_field_dtos_with_field_type_searchable
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos
            =permission_task_gof_field_dtos_with_field_type_searchable
        )
        return task_details_dto

    @pytest.fixture
    def task_complete_details_dto_with_field_type_searchable(
            self, stages_and_actions_details_dtos,
            permission_task_details_dto_with_fields_searchable_type,
            stage_assignee_details_dtos
    ):
        from ib_tasks.interactors.presenter_interfaces \
            .get_task_presenter_interface \
            import TaskCompleteDetailsDTO
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_details_dto=permission_task_details_dto_with_fields_searchable_type,
            stages_and_actions_details_dtos=stages_and_actions_details_dtos,
            stage_assignee_details_dtos=stage_assignee_details_dtos
        )
        return task_complete_details_dto

    @patch.object(GetTaskStagesAndActions, "get_task_stages_and_actions")
    @patch.object(GetTaskBaseInteractor, 'get_task')
    @patch.object(GetStagesAssigneesDetailsInteractor,
                  "get_stages_assignee_details_dtos")
    def test_given_valid_task_and_some_of_fields_are_searchable_returns_task_complete_details_dto(
            self, stage_assignee_details_dtos_mock, get_task_mock,
            get_task_stages_and_actions_mock, mocker,
            task_details_dto_with_some_fields_searchable_type,
            stage_assignee_details_dtos, stages_and_actions_details_dtos,
            user_roles, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            mock_object, permission_gof_ids, reset_sequence,
            permission_task_gof_field_dtos_with_field_type_searchable,
            field_searchable_dtos,
            task_complete_details_dto_with_field_type_searchable
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        from ib_tasks.tests.common_fixtures.adapters \
            .searchable_details_service import \
            searchable_details_dtos_mock
        searchable_details_dtos_mock_method = searchable_details_dtos_mock(
            mocker)
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = \
            task_details_dto_with_some_fields_searchable_type
        stage_assignee_details_dtos_mock.return_value = \
            stage_assignee_details_dtos
        get_task_stages_and_actions_mock.return_value = \
            stages_and_actions_details_dtos
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        task_crud_storage_mock.get_field_searchable_dtos.return_value = \
            field_searchable_dtos
        presenter_mock.get_task_response.return_value = mock_object

        # Act
        interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(
            field_ids, user_roles)
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.assert_called_once()
        searchable_details_dtos_mock_method.assert_called_once()
        presenter_mock.get_task_response.assert_called_once_with(
            task_complete_details_dto_with_field_type_searchable)

    @patch.object(SearchableDetailsService, 'get_searchable_details_dtos')
    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_and_some_of_fields_are_searchable_with_invalid_city_ids_raise_exception(
            self, get_task_mock, get_searchable_details_dtos_mock, mocker,
            task_details_dto_with_some_fields_searchable_type,
            stage_assignee_details_dtos, stages_and_actions_details_dtos,
            user_roles, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            mock_object, permission_gof_ids, reset_sequence,
            permission_task_gof_field_dtos_with_field_type_searchable,
            field_searchable_dtos_with_invalid_city_ids,
            task_complete_details_dto_with_field_type_searchable
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        invalid_city_ids = [100, 110]
        exception_object = InvalidCityIdsException(invalid_city_ids)
        get_searchable_details_dtos_mock.side_effect = exception_object
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = \
            task_details_dto_with_some_fields_searchable_type
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        task_crud_storage_mock.get_field_searchable_dtos.return_value = \
            field_searchable_dtos_with_invalid_city_ids
        presenter_mock.raise_invalid_searchable_records_found.return_value = \
            mock_object

        # Act
        response = interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
                gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(
                field_ids, user_roles)
        presenter_mock.raise_invalid_searchable_records_found \
            .assert_called_once()
        task_crud_storage_mock.get_field_searchable_dtos.assert_called_once()

    @patch.object(SearchableDetailsService, 'get_searchable_details_dtos')
    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_and_some_of_fields_are_searchable_with_invalid_state_ids_raise_exception(
            self, get_task_mock, get_searchable_details_dtos_mock, mocker,
            task_details_dto_with_some_fields_searchable_type,
            stage_assignee_details_dtos, stages_and_actions_details_dtos,
            user_roles, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            mock_object, permission_gof_ids, reset_sequence,
            permission_task_gof_field_dtos_with_field_type_searchable,
            task_complete_details_dto_with_field_type_searchable
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        searchable_field_ids = ["field0", "field2"]
        field_response = ["200", "300"]
        invalid_state_ids = [200]
        field_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            field_id=factory.Iterator(searchable_field_ids),
            field_value=Searchable.STATE.value,
            field_response=factory.Iterator(field_response),
            size=2
        )
        exception_object = InvalidStateIdsException(invalid_state_ids)
        get_searchable_details_dtos_mock.side_effect = exception_object
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = \
            task_details_dto_with_some_fields_searchable_type
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        task_crud_storage_mock.get_field_searchable_dtos.return_value = \
            field_searchable_dtos
        presenter_mock.raise_invalid_searchable_records_found.return_value = \
            mock_object

        # Act
        response = interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
                gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(field_ids, user_roles)
        presenter_mock.raise_invalid_searchable_records_found \
            .assert_called_once()
        task_crud_storage_mock.get_field_searchable_dtos.assert_called_once()

    @patch.object(SearchableDetailsService, 'get_searchable_details_dtos')
    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_and_some_of_fields_are_searchable_with_invalid_country_ids_raise_exception(
            self, get_task_mock, get_searchable_details_dtos_mock, mocker,
            task_details_dto_with_some_fields_searchable_type,
            stage_assignee_details_dtos, stages_and_actions_details_dtos,
            user_roles, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            mock_object, permission_gof_ids, reset_sequence,
            permission_task_gof_field_dtos_with_field_type_searchable,
            task_complete_details_dto_with_field_type_searchable
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        searchable_field_ids = ["field0", "field2"]
        field_response = ["200", "300"]
        invalid_country_ids = [200]
        field_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            field_id=factory.Iterator(searchable_field_ids),
            field_value=Searchable.COUNTRY.value,
            field_response=factory.Iterator(field_response),
            size=2
        )
        exception_object = InvalidCountryIdsException(invalid_country_ids)
        get_searchable_details_dtos_mock.side_effect = exception_object
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = \
            task_details_dto_with_some_fields_searchable_type
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        task_crud_storage_mock.get_field_searchable_dtos.return_value = \
            field_searchable_dtos
        presenter_mock.raise_invalid_searchable_records_found.return_value = \
            mock_object

        # Act
        response = interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(field_ids, user_roles)
        presenter_mock.raise_invalid_searchable_records_found \
            .assert_called_once()
        task_crud_storage_mock.get_field_searchable_dtos.assert_called_once()

    @patch.object(SearchableDetailsService, 'get_searchable_details_dtos')
    @patch.object(GetTaskBaseInteractor, 'get_task')
    def test_given_valid_task_and_some_of_fields_are_searchable_with_invalid_user_ids_raise_exception(
            self, get_task_mock, get_searchable_details_dtos_mock, mocker,
            task_details_dto_with_some_fields_searchable_type,
            stage_assignee_details_dtos, stages_and_actions_details_dtos,
            user_roles, storage_mock, presenter_mock, stages_storage_mock,
            task_storage_mock, task_crud_storage_mock, action_storage_mock,
            task_stage_storage_mock, gof_ids,
            permission_task_gof_dtos, field_ids, permission_field_ids,
            mock_object, permission_gof_ids, reset_sequence,
            permission_task_gof_field_dtos_with_field_type_searchable,
            task_complete_details_dto_with_field_type_searchable
    ):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        searchable_field_ids = ["field0", "field2"]
        field_response = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001"
        ]
        invalid_user_ids = ["123e4567-e89b-12d3-a456-426614174000"]
        field_searchable_dtos = FieldSearchableDTOFactory.create_batch(
            field_id=factory.Iterator(searchable_field_ids),
            field_value=Searchable.USER.value,
            field_response=factory.Iterator(field_response),
            size=2
        )
        exception_object = InvalidUserIdsException(invalid_user_ids)
        get_searchable_details_dtos_mock.side_effect = exception_object
        user_id = "user1"
        task_id = 1
        task_display_id = "IBWF-1"
        get_task_mock.return_value = \
            task_details_dto_with_some_fields_searchable_type
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        task_stage_storage_mock \
            .is_user_has_permission_for_at_least_one_stage.return_value = True
        interactor = GetTaskInteractor(
            storage=storage_mock, stages_storage=stages_storage_mock,
            task_storage=task_storage_mock, action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_crud_storage=task_crud_storage_mock
        )
        task_crud_storage_mock.get_gof_ids_having_permission.return_value = \
            permission_gof_ids
        task_crud_storage_mock.get_field_ids_having_permission.return_value = \
            permission_field_ids
        task_crud_storage_mock.get_field_searchable_dtos.return_value = \
            field_searchable_dtos
        presenter_mock.raise_invalid_searchable_records_found.return_value = \
            mock_object

        # Act
        response = interactor.get_task_details_wrapper(
            user_id=user_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == mock_object
        get_user_role_ids_mock_method.assert_called_once()
        task_crud_storage_mock.get_gof_ids_having_permission \
            .assert_called_once_with(
            gof_ids, user_roles)
        task_crud_storage_mock.get_field_ids_having_permission \
            .assert_called_once_with(field_ids, user_roles)
        presenter_mock.raise_invalid_searchable_records_found \
            .assert_called_once()
        task_crud_storage_mock.get_field_searchable_dtos.assert_called_once()
