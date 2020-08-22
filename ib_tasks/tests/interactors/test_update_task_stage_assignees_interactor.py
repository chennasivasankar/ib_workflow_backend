from unittest.mock import Mock

import mock
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.interactors.stages_dtos import TaskDisplayIdWithStageAssigneesDTO

from ib_tasks.tests.factories.storage_dtos import StageRoleDTOFactory


class TestUpdateTaskStageAssigneesInteractor:
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        stage_storage = mock.create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            update_task_stage_assignees_presenter_interface import \
            UpdateTaskStageAssigneesPresenterInterface
        presenter = mock.create_autospec(
            UpdateTaskStageAssigneesPresenterInterface)
        return presenter

    @pytest.fixture
    def task_id_with_duplicate_stage_assignees_dto(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        task_id_with_stage_assignees_dto = TaskDisplayIdWithStageAssigneesDTO(
            task_display_id="task_1",
            stage_assignees=[
                StageAssigneeDTOFactory(),
                StageAssigneeDTOFactory(db_stage_id=1)
            ])
        return task_id_with_stage_assignees_dto

    @pytest.fixture
    def stage_role_dtos(self):
        StageRoleDTOFactory.reset_sequence()
        stage_role_dtos = StageRoleDTOFactory.create_batch(
            2, role_id=ALL_ROLES_ID)
        return stage_role_dtos

    @pytest.fixture
    def task_display_id_with_stage_assignees_dto(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        task_display_id_with_stage_assignees_dto = \
            TaskDisplayIdWithStageAssigneesDTO(
                task_display_id="task_1",
                stage_assignees=StageAssigneeDTOFactory.create_batch(2))
        return task_display_id_with_stage_assignees_dto

    @pytest.fixture
    def stage_id_with_value_dtos(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageIdWithValueDTOFactory
        StageIdWithValueDTOFactory.reset_sequence()
        stage_id_with_value_dtos = StageIdWithValueDTOFactory.create_batch(2)

        return stage_id_with_value_dtos

    @pytest.fixture
    def task_display_id_with_none_stage_assignees_dto(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        task_display_id_with_stage_assignees_dto = \
            TaskDisplayIdWithStageAssigneesDTO(
                task_display_id="task_1",
                stage_assignees=[StageAssigneeDTOFactory(assignee_id=None),
                                 StageAssigneeDTOFactory()])
        return task_display_id_with_stage_assignees_dto

    def test_given_invalid_task_display_id_raise_exception(
            self, task_storage_mock, stage_storage_mock,
            task_display_id_with_stage_assignees_dto, presenter_mock):
        given_task_display_id = "task_1"
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor

        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto=
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)
        # Assert
        task_storage_mock.check_is_valid_task_display_id \
            .assert_called_once_with(given_task_display_id)
        presenter_mock.raise_invalid_task_display_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_display_id.call_args
        error_object = call_args[0][0]
        invalid_task_display_id = error_object.task_display_id
        assert invalid_task_display_id == given_task_display_id

    def test_given_duplicate_stage_ids_raise_exception(
            self, task_storage_mock, stage_storage_mock,
            task_id_with_duplicate_stage_assignees_dto, presenter_mock):
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto=
            task_id_with_duplicate_stage_assignees_dto,
            presenter=presenter_mock)
        presenter_mock.raise_duplicate_stage_ids_not_valid. \
            assert_called_once_with(duplicate_stage_ids=[1])

    def test_given_invalid_stage_ids_along_with_virtual_stage_ids_raise_exception(
            self, task_storage_mock, stage_storage_mock,
            task_display_id_with_stage_assignees_dto, presenter_mock):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageIdWithValueDTOFactory
        StageIdWithValueDTOFactory.reset_sequence()
        stage_id_with_value_dtos = [StageIdWithValueDTOFactory(),
                                    StageIdWithValueDTOFactory(db_stage_id=3,
                                                               stage_value=-1)]
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_stage_ids_exception. \
            assert_called_once_with(invalid_stage_ids=[2])

    def test_given_virtual_stage_ids_raise_exception(
            self, task_storage_mock, stage_storage_mock,
            task_display_id_with_stage_assignees_dto, presenter_mock):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            StageIdWithValueDTOFactory
        StageIdWithValueDTOFactory.reset_sequence()
        stage_id_with_value_dtos = [StageIdWithValueDTOFactory(),
                                    StageIdWithValueDTOFactory(stage_value=-1)]
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)

        # Assert
        presenter_mock.raise_virtual_stage_ids_exception. \
            assert_called_once_with(virtual_stage_ids=[2])

    def test_given_invalid_user_id_in_assignee_raise_exception(
            self, mocker, stage_storage_mock, task_storage_mock,
            presenter_mock, task_display_id_with_stage_assignees_dto,
            stage_id_with_value_dtos):
        # Arrange
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids_exception
        get_user_role_ids_mock_method = get_user_role_ids_exception(
            mocker, user_id="user_2")
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)
        presenter_mock.raise_invalid_user_id_exception.assert_called_once_with(
            user_id="user_2")

    def test_given_invalid_user_permission_for_stages_raise_exception(
            self, mocker, stage_storage_mock, task_storage_mock,
            presenter_mock, task_display_id_with_stage_assignees_dto,
            stage_id_with_value_dtos):
        StageRoleDTOFactory.reset_sequence()
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_required_user_role_ids
        get_user_role_ids_mock_method = get_required_user_role_ids(
            mocker,
            user_role_ids=['FIN_PAYMENT_POC', 'FIN_COMPLIANCE_VERIFIER'])
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value \
            = StageRoleDTOFactory.create_batch(2)
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)

        presenter_mock. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception. \
            assert_called_once_with(invalid_stage_ids=[1, 2])

    def test_given_stages_having_same_assignees_in_db(
            self, mocker, stage_role_dtos, stage_storage_mock,
            task_storage_mock, presenter_mock,
            task_display_id_with_stage_assignees_dto,
            stage_id_with_value_dtos):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskIdWithStageAssigneeDTOFactory
        TaskIdWithStageAssigneeDTOFactory.reset_sequence(1)
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.\
            return_value = stage_role_dtos
        stage_storage_mock. \
            get_task_stages_having_assignees_without_having_left_at_status. \
            return_value = [StageAssigneeDTOFactory()]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)
        stage_storage_mock. \
            update_task_stages_other_than_matched_stages_with_left_at_status. \
            assert_called_once_with(task_id=1, db_stage_ids=[1])
        stage_storage_mock.create_task_stage_assignees.assert_called_once_with(
            task_id_with_stage_assignee_dtos=
            [TaskIdWithStageAssigneeDTOFactory(task_id=1)])

    def test_given_stages_having_none_assignees_in_db(
            self, mocker, stage_role_dtos, stage_storage_mock,
            task_storage_mock, presenter_mock,
            task_display_id_with_none_stage_assignees_dto,
            stage_id_with_value_dtos):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskIdWithStageAssigneeDTOFactory
        TaskIdWithStageAssigneeDTOFactory.reset_sequence(1)
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids.return_value \
            = stage_role_dtos
        stage_storage_mock. \
            get_task_stages_having_assignees_without_having_left_at_status. \
            return_value = [StageAssigneeDTOFactory(assignee_id=None)]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_none_stage_assignees_dto,
            presenter=presenter_mock)
        stage_storage_mock. \
            update_task_stages_other_than_matched_stages_with_left_at_status. \
            assert_called_once_with(task_id=1, db_stage_ids=[1])
        stage_storage_mock.create_task_stage_assignees.assert_called_once_with(
            task_id_with_stage_assignee_dtos=
            [TaskIdWithStageAssigneeDTOFactory(task_id=1
                )])

    def test_given_stages_having_different_assignees_in_db(
            self, mocker, stage_role_dtos, stage_storage_mock,
            task_storage_mock, presenter_mock,
            task_display_id_with_stage_assignees_dto,
            stage_id_with_value_dtos):
        from ib_tasks.tests.factories.interactor_dtos import \
            StageAssigneeDTOFactory
        StageAssigneeDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskIdWithStageAssigneeDTOFactory
        TaskIdWithStageAssigneeDTOFactory.reset_sequence()
        task_storage_mock.check_is_task_exists.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        stage_storage_mock. \
            get_valid_db_stage_ids_with_stage_value.return_value = \
            stage_id_with_value_dtos
        stage_storage_mock.get_stage_role_dtos_given_db_stage_ids. \
            return_value = stage_role_dtos
        stage_storage_mock. \
            get_task_stages_having_assignees_without_having_left_at_status. \
            return_value = [StageAssigneeDTOFactory(assignee_id='user_3')]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        from ib_tasks.interactors.update_task_stage_assignees_interactor \
            import UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        # Act
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_display_id_with_stage_assignees_dto, presenter=presenter_mock)
        stage_storage_mock. \
            update_task_stages_other_than_matched_stages_with_left_at_status. \
            assert_called_once_with(task_id=1, db_stage_ids=[])
        stage_storage_mock.create_task_stage_assignees.assert_called_once_with(
            task_id_with_stage_assignee_dtos=
            TaskIdWithStageAssigneeDTOFactory.create_batch(2, task_id=1))
