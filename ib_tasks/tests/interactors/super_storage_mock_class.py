from unittest.mock import create_autospec

import pytest


class StorageMockClass:

    @staticmethod
    @pytest.fixture()
    def storage():
        from ib_tasks.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def create_or_update_task_storage():
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        storage = create_autospec(CreateOrUpdateTaskStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def gof_storage():
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        storage = create_autospec(GoFStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def field_storage():
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import FieldsStorageInterface
        storage = create_autospec(FieldsStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def task_template_storage():
        from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
            import TaskTemplateStorageInterface
        storage = create_autospec(TaskTemplateStorageInterface)
        return storage

    @staticmethod
    @pytest.fixture()
    def stage_storage():
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import StageStorageInterface
        storage = create_autospec(StageStorageInterface)
        return storage

    @pytest.fixture
    def elasticsearch_storage(self):
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticSearchStorageInterface
        return create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def task_stage_storage(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return create_autospec(TaskStageStorageInterface)

    @staticmethod
    def gof_and_fields_mock(mocker, task_dto):
        path = 'ib_tasks.interactors.get_task_base_interactor' \
               '.GetTaskBaseInteractor.get_task'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_dto
        return mock_obj

    @staticmethod
    @pytest.fixture()
    def board_mock(mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture
    def task_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return create_autospec(ActionStorageInterface)

    @pytest.fixture
    def elasticsearch_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import \
            ElasticSearchStorageInterface
        return create_autospec(ElasticSearchStorageInterface)

    @staticmethod
    def task_boards_mock(mocker, task_board_details):
        path = 'ib_tasks.adapters.boards_service.BoardsService' \
               '.get_display_boards_and_column_details'

        mock_obj = mocker.patch(path)
        mock_obj.return_value = task_board_details
        return mock_obj

    @staticmethod
    def actions_dto_mock(mocker, actions_dto):
        path = 'ib_tasks.interactors.get_user_permitted_stage_actions' \
               '.GetUserPermittedStageActions' \
               '.get_user_permitted_stage_actions'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = actions_dto
        return mock_obj

    @pytest.fixture
    def get_task_current_stages_mock(self, mocker):
        path = "ib_tasks.interactors.get_task_current_stages_interactor" \
               ".GetTaskCurrentStagesInteractor" \
               ".get_task_current_stages_details"
        return mocker.patch(path)

    @staticmethod
    def fields_mock(mocker, fields_dto):
        path = 'ib_tasks.interactors.get_field_details.GetFieldsDetails' \
               '.get_fields_details'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = fields_dto
        return mock_obj