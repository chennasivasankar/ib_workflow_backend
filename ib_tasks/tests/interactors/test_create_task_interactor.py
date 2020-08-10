import datetime

import mock
import pytest

from ib_tasks.interactors.create_or_update_task.create_task_interactor import \
    CreateTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import GoFFieldsDTOFactory
from ib_tasks.tests.factories.storage_dtos import CreateTaskDTOFactory


class TestCreateTaskInteractor:

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
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.create_task_presenter \
            import CreateTaskPresenterInterface
        return mock.create_autospec(CreateTaskPresenterInterface)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    def test_with_invalid_task_template_id(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        template_id = "template_id"
        task_dto = CreateTaskDTOFactory(task_template_id=template_id)
        task_template_storage_mock.check_is_template_exists.return_value = \
            False
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_invalid_task_template_ids \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        task_template_storage_mock.check_is_template_exists \
            .assert_called_once_with(template_id=template_id)
        presenter_mock.raise_invalid_task_template_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_template_ids.call_args
        error_object = call_args[0][0]
        invalid_template_id = error_object.invalid_task_template_ids[0]
        assert invalid_template_id == template_id

    def test_with_invalid_action_id(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        action_id = "action_id"
        task_dto = CreateTaskDTOFactory(action_id=action_id)
        task_template_storage_mock.check_is_template_exists.return_value = \
            True
        storage_mock.validate_action.return_value = False
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_invalid_action_id.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        storage_mock.validate_action.assert_called_once_with(
            action_id=action_id)
        presenter_mock.raise_invalid_action_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_action_id.call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == action_id

    def test_with_duplicate_same_gof_order_for_a_gof(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_id = "gof_0"
        same_gof_order = 1
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=gof_id, same_gof_order=same_gof_order
        )

        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        task_template_storage_mock.check_is_template_exists.return_value = \
            True
        storage_mock.validate_action.return_value = True
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .assert_called_once()
        call_args = presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .call_args
        error_object = call_args[0][0]
        same_orders_gof_id = error_object.gof_id
        duplicate_same_gof_orders = error_object.same_gof_orders
        assert same_orders_gof_id == gof_id
        assert duplicate_same_gof_orders == [same_gof_order]

    def test_with_start_date_is_ahead_of_due_date(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        start_date = datetime.date(2020, 7, 4)
        due_date = datetime.date(2020, 1, 4)
        task_dto = CreateTaskDTOFactory(
            start_date=start_date, due_date=due_date)
        task_template_storage_mock.check_is_template_exists.return_value = \
            True
        storage_mock.validate_action.return_value = True
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .assert_called_once()
        call_args = presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .call_args
        error_object = call_args[0][0]
        same_orders_gof_id = error_object.gof_id
        duplicate_same_gof_orders = error_object.same_gof_orders
        assert same_orders_gof_id == gof_id
        assert duplicate_same_gof_orders == [same_gof_order]
