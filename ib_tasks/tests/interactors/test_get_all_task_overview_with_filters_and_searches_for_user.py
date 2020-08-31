"""
Created on: 08/08/20
Author: Pavankumar Pamuru

"""
import pytest

from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.tests.common_fixtures.interactors import \
    prepare_get_stage_ids_for_user
from ib_tasks.tests.factories.presenter_dtos import \
    TaskWithCompleteStageDetailsDTOFactory, TaskIdWithStageDetailsDTOFactory


class TestGetTasksOverviewForUserInteractor:

    @classmethod
    def setup_class(cls):
        TaskIdWithStageDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.interactor_dtos import \
            FieldDetailsDTOFactory
        FieldDetailsDTOFactory.reset_sequence()
        from ib_tasks.tests.factories.storage_dtos import \
            StageActionDetailsDTOFactory
        StageActionDetailsDTOFactory.reset_sequence()

    @classmethod
    def teardown_class(cls):
        pass

    @pytest.fixture
    def stage_storage(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        from unittest.mock import create_autospec
        stage_storage = create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_stage_storage(self):
        from unittest.mock import create_autospec
        task_stage_storage = create_autospec(TaskStageStorageInterface)
        return task_stage_storage

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        from unittest.mock import create_autospec
        task_storage = create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def field_storage(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
            FieldsStorageInterface
        from unittest.mock import create_autospec
        field_storage = create_autospec(FieldsStorageInterface)
        return field_storage

    @pytest.fixture
    def action_storage(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        from unittest.mock import create_autospec
        action_storage = create_autospec(ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def task_actions_fields(self):
        from ib_tasks.interactors.storage_interfaces.stage_dtos import \
            GetTaskStageCompleteDetailsDTO
        from ib_tasks.tests.factories.interactor_dtos import \
            FieldDetailsDTOFactory
        from ib_tasks.tests.factories.storage_dtos import \
            StageActionDetailsDTOFactory
        response = [
            GetTaskStageCompleteDetailsDTO(
                task_id=1,
                stage_id="stage_id_1",
                db_stage_id=1,
                display_name="name",
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(2),
                action_dtos=StageActionDetailsDTOFactory.create_batch(2)
            ),
            GetTaskStageCompleteDetailsDTO(
                task_id=1,
                stage_id="stage_id_2",
                db_stage_id=20,
                display_name="name",
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(2),
                action_dtos=StageActionDetailsDTOFactory.create_batch(2)
            ),
            GetTaskStageCompleteDetailsDTO(
                task_id=2,
                stage_id="stage_id_1",
                db_stage_id=1,
                display_name="name",
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(2),
                action_dtos=StageActionDetailsDTOFactory.create_batch(2)
            ),
            GetTaskStageCompleteDetailsDTO(
                task_id=2,
                stage_id="stage_id_2",
                db_stage_id=20,
                display_name="name",
                stage_color="blue",
                field_dtos=FieldDetailsDTOFactory.create_batch(2),
                action_dtos=StageActionDetailsDTOFactory.create_batch(2)
            )
        ]
        return response

    @pytest.fixture
    def expected_response(self):
        return []

    @pytest.fixture
    def stage_ids_dto(self):
        stage_ids_dto = TaskWithCompleteStageDetailsDTOFactory.create_batch(2)
        return stage_ids_dto

    def test_get_filtered_tasks_overview_with_invalid_project_id(
            self, mocker, stage_storage, task_storage, field_storage,
            action_storage, task_stage_storage):
        # Arrange
        user_id = 'user_id'
        task_ids = [1, 2, 3]
        project_id = '1'
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value

        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        project_id_validation_mock = get_valid_project_ids_mock(
            mocker=mocker, project_ids=[]
        )

        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor

        interactor = GetTasksOverviewForUserInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            field_storage=field_storage,
            action_storage=action_storage,
            task_stage_storage=task_stage_storage
        )

        # Act
        from ib_tasks.exceptions.adapter_exceptions import \
            InvalidProjectIdsException
        with pytest.raises(InvalidProjectIdsException) as error:
            interactor.get_filtered_tasks_overview_for_user(
                user_id=user_id,
                task_ids=task_ids,
                view_type=view_type,
                project_id=project_id
            )

        # Assert
        project_id_validation_mock.assert_called_once_with([project_id])
        assert error.value.invalid_project_ids == [project_id]

    def test_get_filtered_tasks_overview_with_user_not_in_project_id(
            self, mocker, stage_storage, task_storage, field_storage,
            action_storage, task_stage_storage):
        # Arrange
        user_id = 'user_id'
        task_ids = [1, 2, 3]
        project_id = '1'
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value

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

        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor

        interactor = GetTasksOverviewForUserInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            field_storage=field_storage,
            action_storage=action_storage,
            task_stage_storage=task_stage_storage
        )

        # Act
        from ib_tasks.exceptions.adapter_exceptions import \
            UserIsNotInProjectException
        with pytest.raises(UserIsNotInProjectException) as error:
            interactor.get_filtered_tasks_overview_for_user(
                user_id=user_id,
                task_ids=task_ids,
                view_type=view_type,
                project_id=project_id
            )

        # Assert
        project_id_validation_mock.assert_called_once_with([project_id])
        user_in_project_validation_mock.assert_called_once_with(
            user_id=user_id, project_id=project_id
        )

    def test_get_filtered_tasks_overview_with_task_ids_not_in_project_id(
            self, mocker, stage_storage, task_storage, field_storage,
            action_storage, task_stage_storage):
        # Arrange
        user_id = 'user_id'
        task_ids = [1, 2, 3]
        valid_task_ids = [1, 2]
        invalid_task_ids = [3]
        project_id = '1'
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value

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
        task_storage.get_valid_task_ids_from_the_project.return_value = valid_task_ids
        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor, TaskIdsNotInProject

        interactor = GetTasksOverviewForUserInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            field_storage=field_storage,
            action_storage=action_storage,
            task_stage_storage=task_stage_storage
        )

        # Act
        with pytest.raises(TaskIdsNotInProject) as error:
            interactor.get_filtered_tasks_overview_for_user(
                user_id=user_id,
                task_ids=task_ids,
                view_type=view_type,
                project_id=project_id
            )

        # Assert
        task_storage.get_valid_task_ids_from_the_project.assert_called_once_with(
            task_ids=task_ids, project_id=project_id
        )
        assert error.value.invalid_task_ids == invalid_task_ids

    def test_get_filtered_tasks_overview_for_user_with_valid_details(
            self, mocker, task_actions_fields, expected_response, stage_storage, snapshot,
            task_storage, field_storage, action_storage, task_stage_storage, stage_ids_dto):
        # Arrange
        user_id = 'user_id'
        task_ids = [1, 2]
        project_id = '1'

        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user \
            import GetTasksOverviewForUserInteractor

        interactor = GetTasksOverviewForUserInteractor(
            stage_storage=stage_storage,
            task_storage=task_storage,
            field_storage=field_storage,
            action_storage=action_storage,
            task_stage_storage=task_stage_storage
        )
        fields_and_actions = task_actions_fields
        stage_ids = ['stage_id_1', "stage_id_2"]
        prepare_get_stage_ids_for_user(mocker, stage_ids)
        from ib_tasks.tests.common_fixtures.interactors import \
            prepare_task_ids_with_stage_ids
        prepare_task_ids_with_stage_ids(
            mocker=mocker,
            stage_ids_dto=stage_ids_dto,
            fields_and_actions=fields_and_actions,
            stage_ids=stage_ids
        )
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
        task_storage.get_valid_task_ids_from_the_project.return_value = task_ids
        from ib_tasks.constants.enum import ViewType
        view_type = ViewType.KANBAN.value

        # Act
        actual_response = interactor.get_filtered_tasks_overview_for_user(
            user_id=user_id,
            task_ids=task_ids,
            view_type=view_type,
            project_id=project_id
        )

        # Assert
        snapshot.assert_match(actual_response,'tasks_in_a_project')


