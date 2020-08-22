import pytest
from mock import create_autospec

from ib_tasks.interactors.get_task_current_stages_interactor import \
    GetTaskCurrentStagesInteractor
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service \
    import get_user_role_ids


class TestGetTaskCurrentStagesInteractor:

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def stage_details_dtos(self):
        from ib_tasks.tests.factories.storage_dtos import \
            CurrentStageDetailsDTOFactory
        stage_details_dtos = CurrentStageDetailsDTOFactory.create_batch(size=3)
        return stage_details_dtos

    @pytest.fixture
    def user_roles(self):
        user_roles = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
                      'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                      'FIN_COMPLIANCE_APPROVER',
                      'FIN_PAYMENTS_LEVEL1_VERIFIER',
                      'FIN_PAYMENTS_LEVEL2_VERIFIER',
                      'FIN_PAYMENTS_LEVEL3_VERIFIER',
                      'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                      'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                      'FIN_ACCOUNTS_LEVEL2_VERIFIER']
        return user_roles

    def test_given_invalid_task_id_raise_exception(
            self, task_stage_storage_mock
    ):
        # Arrange
        task_id = 2
        user_id = "1234567fbdg56756"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        error_obj = InvalidTaskIdException(task_id)
        task_stage_storage_mock.validate_task_id.side_effect = error_obj

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            interactor.get_task_current_stages_details(
                task_id=task_id, user_id=user_id
            )

        # Assert
        exception_object = err.value
        assert exception_object.task_id == error_obj.task_id

    def test_given_valid_task_id_returns_task_display_name(
            self, task_stage_storage_mock, mocker
    ):
        # Arrange

        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id

        # Act
        interactor.get_task_current_stages_details(
            task_id=task_id, user_id=user_id
        )

        # Assert
        task_stage_storage_mock.validate_task_id.assert_called_once_with(
            task_id
        )

    def test_given_valid_task_ids_return_task_current_stage_ids(
            self, task_stage_storage_mock, mocker
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        stage_ids = [1, 2, 3]
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids

        # Act
        interactor.get_task_current_stages_details(
            task_id=task_id, user_id=user_id
        )

        # Assert
        task_stage_storage_mock.get_task_current_stage_ids \
            .assert_called_once_with(
            task_id)

    def test_given_task_id_and_stage_ids_returns_stage_details_dtos(
            self, task_stage_storage_mock, stage_details_dtos, mocker
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        stage_ids = [1, 2, 3]
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids
        task_stage_storage_mock.get_stage_details_dtos.return_value = \
            stage_details_dtos

        # Act
        interactor.get_task_current_stages_details(task_id=task_id,
                                                   user_id=user_id)

        # Assert
        task_stage_storage_mock.get_stage_details_dtos.assert_called_once_with(
            stage_ids=stage_ids
        )
        get_user_role_ids_mock_method.assert_called_once()

    def test_given_stage_ids_and_user_roles_if_user_has_no_permission_for_stages_returns_false(
            self, task_stage_storage_mock,
            stage_details_dtos, mocker, user_roles
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        stage_ids = [1, 2, 3]
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids
        task_stage_storage_mock.get_stage_details_dtos.return_value = \
            stage_details_dtos
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .return_value = False

        # Act
        interactor.get_task_current_stages_details(task_id=task_id,
                                                   user_id=user_id)

        # Assert
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .assert_called_once_with(
            stage_ids=stage_ids, user_roles=user_roles
        )

    def test_given_stage_ids_and_user_roles_if_user_has_permission_for_stages_returns_true(
            self, task_stage_storage_mock,
            stage_details_dtos, mocker, user_roles
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        stage_ids = [1, 2, 3]
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids
        task_stage_storage_mock.get_stage_details_dtos.return_value = \
            stage_details_dtos
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .return_value = True

        # Act
        interactor.get_task_current_stages_details(task_id=task_id,
                                                   user_id=user_id)

        # Assert
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .assert_called_once_with(
            stage_ids=stage_ids, user_roles=user_roles
        )

    def test_given_valid_details_when_user_has_no_permissions_returns_task_current_stage_details_dto(
            self, task_stage_storage_mock, mocker,
            stage_details_dtos, user_roles
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        is_user_has_permission = False
        stage_ids = [1, 2, 3]
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids
        task_stage_storage_mock.get_stage_details_dtos.return_value = \
            stage_details_dtos
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .return_value = is_user_has_permission
        expected_task_current_stage_details_dto = TaskCurrentStageDetailsDTO(
            task_display_id=task_display_id,
            stage_details_dtos=stage_details_dtos,
            user_has_permission=is_user_has_permission,
        )

        # Act
        actual_task_current_stage_details_dto = \
            interactor.get_task_current_stages_details(
                task_id=task_id, user_id=user_id
            )

        # Assert
        assert actual_task_current_stage_details_dto == \
               expected_task_current_stage_details_dto

    def test_given_valid_details_when_user_has_permissions_returns_task_current_stage_details_dto(
            self, task_stage_storage_mock, mocker,
            stage_details_dtos, user_roles
    ):
        # Arrange
        task_id = 2
        task_display_id = "IBWF-1"
        user_id = "1234567fbdg56756"
        is_user_has_permission = True
        stage_ids = [1, 2, 3]
        get_user_role_ids(mocker)
        interactor = GetTaskCurrentStagesInteractor(
            task_stage_storage=task_stage_storage_mock)
        task_stage_storage_mock.validate_task_id.return_value = task_display_id
        task_stage_storage_mock.get_task_current_stage_ids.return_value = \
            stage_ids
        task_stage_storage_mock.get_stage_details_dtos.return_value = \
            stage_details_dtos
        task_stage_storage_mock.is_user_has_permission_for_at_least_one_stage \
            .return_value = is_user_has_permission
        expected_task_current_stage_details_dto = TaskCurrentStageDetailsDTO(
            task_display_id=task_display_id,
            stage_details_dtos=stage_details_dtos,
            user_has_permission=is_user_has_permission,
        )

        # Act
        actual_task_current_stage_details_dto = \
            interactor.get_task_current_stages_details(
            task_id=task_id, user_id=user_id
        )

        # Assert
        assert actual_task_current_stage_details_dto == \
               expected_task_current_stage_details_dto
