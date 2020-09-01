"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""
import pytest


class TestGetTaskIdsOfUserBasedOnStagesInteractor:
    @pytest.fixture()
    def task_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        storage = create_autospec(TaskStorageInterface)
        return storage

    @pytest.fixture()
    def stage_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface

        storage = create_autospec(StageStorageInterface)
        return storage

    @pytest.fixture()
    def task_stage_storage_mock(self):
        from mock import create_autospec

        from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
            TaskStageStorageInterface
        storage = create_autospec(TaskStageStorageInterface)
        return storage

    def test_given_valid_stage_ids_get_tasks_with_invalid_project_id(
            self, task_storage_mock, stage_storage_mock, mocker,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        task_ids = [1, 2]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        project_id_validation_mock = get_valid_project_ids_mock(
            mocker=mocker, project_ids=[]
        )
        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        from ib_tasks.exceptions.adapter_exceptions import \
            InvalidProjectIdsException
        with pytest.raises(InvalidProjectIdsException) as error:
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id,
                stage_ids=valid_stage_ids,
                task_ids=task_ids,
                project_id=project_id
            )

        # Assert
        project_id_validation_mock.assert_called_once_with([project_id])
        assert error.value.invalid_project_ids == [project_id]

    def test_given_valid_stage_ids_get_tasks_with_user_not_in_project_id(
            self, task_storage_mock, stage_storage_mock, mocker,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        task_ids = [1, 2]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        project_id_validation_mock = get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        user_in_project_validation_mock = validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=False
        )
        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        from ib_tasks.exceptions.adapter_exceptions import \
            UserIsNotInProjectException
        with pytest.raises(UserIsNotInProjectException) as error:
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id,
                stage_ids=valid_stage_ids,
                task_ids=task_ids,
                project_id=project_id
            )

        # Assert
        project_id_validation_mock.assert_called_once_with([project_id])
        user_in_project_validation_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )

    def test_given_valid_stage_ids_get_tasks_with_task_ids_not_in_project_id(
            self, task_storage_mock, stage_storage_mock, mocker,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        user_id = 'user_id'
        task_ids = [1, 2, 3]
        valid_task_ids = [1, 2]
        invalid_task_ids = [3]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        project_id_validation_mock = get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        user_in_project_validation_mock = validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        task_storage_mock.get_valid_task_ids_from_the_project.return_value = valid_task_ids
        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskIdsNotInProject
        with pytest.raises(TaskIdsNotInProject) as error:
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id,
                stage_ids=valid_stage_ids,
                task_ids=task_ids,
                project_id=project_id
            )

        # Assert
        project_id_validation_mock.assert_called_once_with([project_id])
        user_in_project_validation_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )
        task_storage_mock.get_valid_task_ids_from_the_project.assert_called_once_with(
            task_ids=task_ids, project_id=project_id
        )
        assert error.value.invalid_task_ids == invalid_task_ids

    def test_given_valid_stage_ids_with_invalid_stages_return_error_message(
            self, task_storage_mock, stage_storage_mock, mocker,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1"]
        stage_ids = ["stage_id_1", "stage_id_2"]
        invalid_stage_ids = ["stage_id_2"]
        task_ids = [1, 2]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        task_storage_mock.get_valid_task_ids_from_the_project.return_value = task_ids
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = valid_stage_ids

        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            return_value = \
            [TaskIdWithStageValueDTO(task_id=1, stage_value=2),
             TaskIdWithStageValueDTO(task_id=2, stage_value=2)]
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(stage_value=2,
                                     task_ids=[1, 2])
        ]

        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        with pytest.raises(InvalidStageIdsListException) as error:
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_id=user_id,
                stage_ids=stage_ids,
                task_ids=task_ids,
                project_id=project_id
            )

        # Assert
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids. \
            assert_called_once_with(user_stages_with_pagination_dto.stage_ids)
        assert error.value.invalid_stage_ids == invalid_stage_ids

    def test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos_with_no_assignees(
            self, task_storage_mock, stage_storage_mock, mocker, snapshot,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        task_ids = [1, 2]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        task_storage_mock.get_valid_task_ids_from_the_project.return_value = task_ids
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = valid_stage_ids
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskIdWithStageDetailsDTOFactory
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        stage_storage_mock.get_task_id_with_stage_details_dtos_based_on_stage_value.\
            return_value = TaskIdWithStageDetailsDTOFactory.create_batch(2)
        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            return_value = \
            [TaskIdWithStageValueDTO(task_id=1, stage_value=2),
             TaskIdWithStageValueDTO(task_id=2, stage_value=2)]
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(stage_value=2,
                                     task_ids=[1, 2])
        ]

        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        actual_response = interactor.get_task_ids_of_user_based_on_stage_ids(
            user_id=user_id,
            stage_ids=valid_stage_ids,
            task_ids=task_ids,
            project_id=project_id
        )

        # Assert
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids. \
            assert_called_once_with(user_stages_with_pagination_dto.stage_ids)
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            assert_called_once_with(stage_ids=valid_stage_ids,
                                    task_ids=task_ids)
        stage_storage_mock.get_task_id_with_stage_details_dtos_based_on_stage_value(
            stage_values=[2],
            task_ids_group_by_stage_value_dtos=task_ids_group_by_stage_value_dtos,
        )
        task_storage_mock.get_valid_task_ids_from_the_project.assert_called_once_with(
            task_ids=task_ids, project_id=project_id
        )
        snapshot.assert_match(actual_response, 'stage_details_for_task_ids')

    def test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos(
            self, task_storage_mock, stage_storage_mock, mocker, snapshot,
            task_stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        task_ids = [1, 2]
        project_id = '1'
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(
            mocker=mocker, project_ids=[project_id]
        )
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(
            mocker=mocker, is_user_in_project=True
        )
        task_storage_mock.get_valid_task_ids_from_the_project.return_value = task_ids
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = valid_stage_ids
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskIdWithStageDetailsDTOFactory
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        stage_storage_mock.get_task_id_with_stage_details_dtos_based_on_stage_value.\
            return_value = TaskIdWithStageDetailsDTOFactory.create_batch(2)
        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            return_value = \
            [TaskIdWithStageValueDTO(task_id=1, stage_value=2),
             TaskIdWithStageValueDTO(task_id=2, stage_value=2)]
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(stage_value=2,
                                     task_ids=[1, 2])
        ]

        from ib_tasks.interactors. \
            get_valid_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        actual_response = interactor.get_task_ids_of_user_based_on_stage_ids(
            user_id=user_id,
            stage_ids=valid_stage_ids,
            task_ids=task_ids,
            project_id=project_id
        )

        # Assert
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids. \
            assert_called_once_with(user_stages_with_pagination_dto.stage_ids)
        task_storage_mock. \
            get_user_task_ids_and_max_stage_value_dto_based_on_given_stage_ids. \
            assert_called_once_with(stage_ids=valid_stage_ids,
                                    task_ids=task_ids)
        stage_storage_mock.get_task_id_with_stage_details_dtos_based_on_stage_value(
            stage_values=[2],
            task_ids_group_by_stage_value_dtos=task_ids_group_by_stage_value_dtos,
        )
        task_storage_mock.get_valid_task_ids_from_the_project.assert_called_once_with(
            task_ids=task_ids, project_id=project_id
        )
        snapshot.assert_match(actual_response, 'stage_details_for_task_ids')
