from unittest.mock import Mock

import mock
import pytest

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.interactors.stages_dtos import TaskIdWithStageAssigneesDTO, \
    StageAssigneeDTO, TaskIdWithStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO
from ib_tasks.tests.factories.interactor_dtos import \
    TaskIdWithStageAssigneeDTOFactory
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
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
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
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=1, stage_assignees=[
                StageAssigneeDTO(db_stage_id=1,
                                 assignee_id="user_1"),
                StageAssigneeDTO(db_stage_id=1,
                                 assignee_id="user_1")])
        return task_id_with_stage_assignees_dto

    @pytest.fixture
    def stage_role_dtos(self):
        StageRoleDTOFactory.reset_sequence()
        stage_role_dtos = StageRoleDTOFactory.create_batch(2,
                                                           role_id=ALL_ROLES_ID)
        return stage_role_dtos

    @pytest.fixture
    def task_id_with_stage_assignees_dto(self):
        task_id_with_stage_assignees_dto = \
            TaskIdWithStageAssigneesDTO(task_id=1, stage_assignees=[
                StageAssigneeDTO(db_stage_id=1,
                                 assignee_id="user_0"),
                StageAssigneeDTO(db_stage_id=2,
                                 assignee_id="user_1")])
        return task_id_with_stage_assignees_dto

    def test_given_invalid_task_id_raise_exception(self, task_storage_mock,
                                                   stage_storage_mock,
                                                   task_id_with_duplicate_stage_assignees_dto,
                                                   presenter_mock):
        task_storage_mock.check_is_task_exists.return_value = False
        presenter_mock.raise_invalid_task_id_exception.return_value = Mock()
        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)

        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_id_with_duplicate_stage_assignees_dto,
            presenter=presenter_mock)
        presenter_mock.raise_invalid_task_id_exception.assert_called_once_with(
            task_id=task_id_with_duplicate_stage_assignees_dto.task_id)

    def test_given_duplicate_stage_ids_raise_exception(self, task_storage_mock,
                                                       stage_storage_mock,
                                                       task_id_with_duplicate_stage_assignees_dto,
                                                       presenter_mock):
        task_storage_mock.check_is_task_exists.return_value = True
        presenter_mock.raise_duplicate_stage_ids_not_valid.return_value = Mock()
        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)

        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_id_with_duplicate_stage_assignees_dto,
            presenter=presenter_mock)
        presenter_mock.raise_duplicate_stage_ids_not_valid.assert_called_once_with(
            duplicate_stage_ids=[1])

    def test_given_invalid_stage_ids_raise_exception(self,
                                                     task_id_with_stage_assignees_dto,
                                                     task_storage_mock,
                                                     stage_storage_mock,
                                                     presenter_mock):
        task_storage_mock.check_is_task_exists.return_value = True
        stage_storage_mock. \
            get_valid_db_stage_ids_excluding_virtual_stages_in_given_db_stage_ids.return_value = [1]
        presenter_mock.raise_invalid_stage_ids_exception.return_value = Mock()
        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)

        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_id_with_stage_assignees_dto,
            presenter=presenter_mock)
        presenter_mock.raise_invalid_stage_ids_exception.assert_called_once_with(
            invalid_stage_ids=[2])

    def test_given_valid_details(self, task_id_with_stage_assignees_dto,
                                 task_storage_mock,
                                 stage_storage_mock,
                                 presenter_mock, stage_role_dtos):
        task_id_with_stage_assignee_dtos = TaskIdWithStageAssigneeDTOFactory. \
            create_batch(2, task_id=1)
        task_storage_mock.check_is_task_exists.return_value = True
        stage_storage_mock. \
            get_valid_db_stage_ids_excluding_virtual_stages_in_given_db_stage_ids.return_value = [
            1, 2]
        stage_storage_mock.create_task_stage_assignees.return_value = None
        stage_storage_mock. \
            get_stage_role_dtos_given_db_stage_ids.return_value = stage_role_dtos
        from ib_tasks.interactors.update_task_stage_assignees_interactor import \
            UpdateTaskStageAssigneesInteractor
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=stage_storage_mock,
                task_storage=task_storage_mock)
        update_task_stage_assignees_interactor. \
            update_task_stage_assignees_wrapper(
            task_id_with_stage_assignees_dto,
            presenter=presenter_mock)

        stage_storage_mock.create_task_stage_assignees.assert_called_once_with(
            task_id_with_stage_assignee_dtos=task_id_with_stage_assignee_dtos)
