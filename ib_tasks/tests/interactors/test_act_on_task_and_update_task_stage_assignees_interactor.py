import mock
import pytest

from ib_tasks.tests.factories.interactor_dtos import StageAssigneeDTOFactory


class TestActOnTaskAndUpdateTaskStageAssigneesInteractor:
    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageAssigneeDTOFactory.reset_sequence()

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        return mock.create_autospec(TaskStorageInterface)

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def create_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        return mock.create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        return mock.create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import StageStorageInterface
        return mock.create_autospec(StageStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def elastic_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticSearchStorageInterface
        return mock.create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return mock.create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            act_on_task_and_upadte_task_stage_assignees_presenter_interface import \
            ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface
        return mock.create_autospec(
            ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface)

    @pytest.fixture
    def user_action_on_task_mock(self, mocker):
        path = "ib_tasks.interactors.user_action_on_task_interactor" \
               ".UserActionOnTaskInteractor.act_on_task"
        return mocker.patch(path)

    @pytest.fixture
    def stage_assignees_dto(self):
        return StageAssigneeDTOFactory.create_batch(2)

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

    def test_given_invalid_task_display_id_raise_exception(
            self, field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId

        task_display_id = "IBWF-1"
        action_id = 1
        board_id = None
        user_id = "user_1"
        exception_object = InvalidTaskDisplayId(task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        presenter_mock.raise_invalid_task_display_id.return_value = \
            mock_object

        # Assert
        call_tuple = presenter_mock.raise_invalid_task_display_id.call_args
        error_obj = call_tuple.args[0]
        assert error_obj.task_display_id == exception_object.task_display_id

