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

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        UserStagesWithPaginationDTOFactory.reset_sequence()

    @pytest.mark.parametrize("limit", [0, -1])
    def test_given_limit_values_less_than_one_raise_exception(
            self, limit, task_storage_mock, stage_storage_mock):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory(
            limit=limit)

        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor

        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)

        # Act
        from ib_tasks.exceptions.fields_custom_exceptions import \
            LimitShouldBeGreaterThanZeroException
        with pytest.raises(LimitShouldBeGreaterThanZeroException):
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_stages_with_pagination_dto)

    @pytest.mark.parametrize("offset", [-1, -2])
    def test_given_offset_values_less_than_zero_raise_exception(
            self, offset, task_storage_mock, stage_storage_mock):
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory(
            offset=offset)

        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor

        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)

        # Act
        from ib_tasks.exceptions.fields_custom_exceptions import \
            OffsetShouldBeGreaterThanZeroException
        with pytest.raises(
                OffsetShouldBeGreaterThanZeroException):
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_stages_with_pagination_dto)

    def test_given_empty_stage_ids_list_raise_exception(
            self, task_storage_mock, stage_storage_mock):
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory(
            stage_ids=[])

        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor

        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)

        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsListEmptyException
        with pytest.raises(StageIdsListEmptyException):
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_stages_with_pagination_dto)

    def test_given_invalid_stage_ids_raise_exception_with_ids(
            self, task_storage_mock, stage_storage_mock):
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = ["stage_id_1", "stage_id_4", "stage_id_5"]

        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor

        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)

        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        with pytest.raises(InvalidStageIdsListException):
            interactor.get_task_ids_of_user_based_on_stage_ids(
                user_stages_with_pagination_dto)
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.assert_called_once_with(
            user_stages_with_pagination_dto.stage_ids)

    def test_given_valid_stage_ids_get_tasks_with_max_stage_value_dtos(
            self, task_storage_mock, stage_storage_mock):
        # Arrange
        valid_stage_ids = ["stage_id_1", "stage_id_2"]
        from ib_tasks.tests.factories.interactor_dtos import \
            UserStagesWithPaginationDTOFactory
        user_stages_with_pagination_dto = UserStagesWithPaginationDTOFactory()
        user_id = user_stages_with_pagination_dto.user_id
        limit = user_stages_with_pagination_dto.offset + \
                user_stages_with_pagination_dto.limit
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.return_value \
            = valid_stage_ids

        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            TaskIdWithStageValueDTO, StageValueWithTaskIdsDTO
        task_storage_mock. \
            get_user_task_and_max_stage_value_dto_based_on_given_stage_ids. \
            return_value = \
            [TaskIdWithStageValueDTO(task_id=1, stage_value=2),
             TaskIdWithStageValueDTO(task_id=2, stage_value=2)]
        task_ids_group_by_stage_value_dtos = [
            StageValueWithTaskIdsDTO(stage_value=2,
                                     task_ids=[1, 2])
        ]

        from ib_tasks.interactors. \
            get_task_ids_of_user_based_on_stage_ids_interactor import \
            GetTaskIdsOfUserBasedOnStagesInteractor
        # Act
        interactor = GetTaskIdsOfUserBasedOnStagesInteractor(
            task_storage=task_storage_mock, stage_storage=stage_storage_mock)
        interactor.get_task_ids_of_user_based_on_stage_ids(
            user_stages_with_pagination_dto)

        # Assert
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids. \
            assert_called_once_with(user_stages_with_pagination_dto.stage_ids)
        task_storage_mock. \
            get_user_task_and_max_stage_value_dto_based_on_given_stage_ids. \
            assert_called_once_with(
            user_id=user_id,
            stage_ids=valid_stage_ids, limit=limit,
            offset=user_stages_with_pagination_dto.offset)
        stage_storage_mock. \
            get_task_id_with_stage_details_dtos_based_on_stage_value(
            stage_values=[2],
            task_ids_group_by_stage_value_dtos=
            task_ids_group_by_stage_value_dtos,
            user_id=user_id)
