import datetime

import factory
import freezegun
import mock
import pytest

from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, UserDidNotFillRequiredGoFs
from ib_tasks.interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ib_tasks.interactors.stages_dtos import TaskIdWithStageAssigneesDTO
from ib_tasks.tests.factories.interactor_dtos import FieldValuesDTOFactory, \
    GoFFieldsDTOFactory, UpdateTaskWithTaskDisplayIdDTOFactory, \
    UpdateTaskDTOFactory, StageAssigneeDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    GoFIdWithSameGoFOrderDTOFactory, FieldIdWithTaskGoFIdDTOFactory, \
    TaskGoFDetailsDTOFactory, TaskGoFFieldDTOFactory, \
    TaskGoFWithTaskIdDTOFactory, FieldIdWithFieldDisplayNameDTOFactory


class TestUpdateTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldValuesDTOFactory.reset_sequence()
        GoFFieldsDTOFactory.reset_sequence()
        UpdateTaskWithTaskDisplayIdDTOFactory.reset_sequence()
        GoFIdWithSameGoFOrderDTOFactory.reset_sequence()
        FieldIdWithTaskGoFIdDTOFactory.reset_sequence()
        TaskGoFDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()
        TaskGoFWithTaskIdDTOFactory.reset_sequence()
        StageAssigneeDTOFactory.reset_sequence()
        FieldIdWithFieldDisplayNameDTOFactory.reset_sequence()

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
    def elastic_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticSearchStorageInterface
        return mock.create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return mock.create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.update_task_presenter \
            import UpdateTaskPresenterInterface
        return mock.create_autospec(UpdateTaskPresenterInterface)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    @pytest.fixture
    def perform_base_validations_for_template_gofs_and_fields_mock(self,
                                                                   mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".template_gofs_fields_base_validations" \
               ".TemplateGoFsFieldsBaseValidationsInteractor" \
               ".perform_base_validations_for_template_gofs_and_fields"
        return mocker.patch(path)

    @pytest.fixture
    def update_task_stage_assignees_mock(self, mocker):
        path = "ib_tasks.interactors.update_task_stage_assignees_interactor" \
               ".UpdateTaskStageAssigneesInteractor" \
               ".update_task_stage_assignees"
        return mocker.patch(path)

    @pytest.fixture
    def get_filtered_tasks_overview_for_user_mock(self, mocker):
        path = \
            "ib_tasks.interactors" \
            ".get_all_task_overview_with_filters_and_searches_for_user" \
            ".GetTasksOverviewForUserInteractor" \
            ".get_filtered_tasks_overview_for_user"
        return mocker.patch(path)

    def test_with_invalid_task_display_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_task_display_id = "task_1"
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_task_display_id.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        task_storage_mock.check_is_valid_task_display_id \
            .assert_called_once_with(
            given_task_display_id)
        presenter_mock.raise_invalid_task_display_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_display_id.call_args
        error_object = call_args[0][0]
        invalid_task_display_id = error_object.task_display_id
        assert invalid_task_display_id == given_task_display_id

    def test_with_invalid_task_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_task_display_id = "task_1"
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = False
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_task_id.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        create_task_storage_mock.is_valid_task_id.assert_called_once_with(
            task_id)
        presenter_mock.raise_invalid_task_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_id.call_args
        error_object = call_args[0][0]
        invalid_task_id = error_object.task_id
        assert invalid_task_id == task_id

    def test_with_invalid_stage_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_task_display_id = "task_1"
        given_stage_id = 2
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id,
            stage_assignee__stage_id=given_stage_id)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        stage_storage_mock.check_is_stage_exists.return_value = False
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock)
        presenter_mock.raise_invalid_stage_id.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        stage_storage_mock.check_is_stage_exists.assert_called_once_with(
            given_stage_id)
        presenter_mock.raise_invalid_stage_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_id.call_args
        error_object = call_args[0][0]
        invalid_stage_id = error_object.stage_id
        assert invalid_stage_id == given_stage_id

    def test_with_priority_none_when_action_type_is_no_validations(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(priority=None)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        stage_storage_mock.check_is_stage_exists.return_value = True
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock)
        presenter_mock.raise_priority_is_required.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_priority_is_required.assert_called_once()

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_due_date_time_without_start_date_time(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_due_date_time = datetime.datetime.now()
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=None, due_datetime=given_due_date_time)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        stage_storage_mock.check_is_stage_exists.return_value = True
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock)
        presenter_mock.raise_due_date_time_without_start_datetime \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_without_start_datetime \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_due_date_time_without_start_datetime.call_args
        error_object = call_args[0][0]
        due_datetime = error_object.due_datetime
        assert due_datetime == given_due_date_time

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_without_start_datetime_when_action_type_is_not_no_validations(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=None, due_datetime=None)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        stage_storage_mock.check_is_stage_exists.return_value = True
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock)
        presenter_mock.raise_start_date_time_is_required \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_time_is_required \
            .assert_called_once()

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_without_due_datetime_when_action_type_is_not_no_validations(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_start_datetime = datetime.datetime.now()
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=given_start_datetime, due_datetime=None)
        task_id = 1
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        stage_storage_mock.check_is_stage_exists.return_value = True
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock)
        presenter_mock.raise_due_date_time_is_required \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_is_required \
            .assert_called_once()

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_date_time(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_start_datetime = datetime.datetime(2020, 8, 20)
        given_due_datetime = datetime.datetime(2020, 9, 1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=given_start_datetime,
            due_datetime=given_due_datetime)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_due_date_time_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired.assert_called_once()
        call_args = presenter_mock.raise_due_date_time_has_expired.call_args
        error_object = call_args[0][0]
        invalid_due_date = error_object.due_datetime
        assert invalid_due_date == given_due_datetime

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_date_time_when_due_date_is_today(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_start_datetime = datetime.datetime(2020, 8, 20)
        given_due_datetime = datetime.datetime(2020, 9, 9, 13, 0, 0)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=given_start_datetime,
            due_datetime=given_due_datetime)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_due_date_time_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired.assert_called_once()
        call_args = presenter_mock.raise_due_date_time_has_expired.call_args
        error_object = call_args[0][0]
        invalid_due_date = error_object.due_datetime
        assert invalid_due_date == given_due_datetime

    def test_with_start_date_ahead_of_due_date(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_start_datetime = datetime.datetime(2020, 9, 9)
        given_due_datetime = datetime.datetime(2020, 9, 1)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=given_start_datetime,
            due_datetime=given_due_datetime)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_start_date_is_ahead_of_due_date \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_is_ahead_of_due_date \
            .assert_called_once()
        call_args = presenter_mock.raise_start_date_is_ahead_of_due_date \
            .call_args
        error_object = call_args[0][0]
        invalid_start_date = error_object.given_start_date
        invalid_due_date = error_object.given_due_date
        assert invalid_start_date == given_start_datetime
        assert invalid_due_date == given_due_datetime

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_time_for_today(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_start_date = datetime.datetime(2020, 9, 1)
        given_due_datetime = datetime.datetime(2020, 9, 9, 13, 0, 0)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            start_datetime=given_start_date,
            due_datetime=given_due_datetime)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_due_date_time_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired \
            .assert_called_once()
        call_args = presenter_mock.raise_due_date_time_has_expired \
            .call_args
        error_object = call_args[0][0]
        invalid_due_datetime = error_object.due_datetime
        assert given_due_datetime == invalid_due_datetime

    def test_with_duplicate_same_gof_orders(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_same_gof_order = 1
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=given_gof_id, same_gof_order=given_same_gof_order)
        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = \
            DuplicateSameGoFOrderForAGoF(given_gof_id, [given_same_gof_order])
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = DuplicateSameGoFOrderForAGoF(
            given_gof_id, [given_same_gof_order])
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .assert_called_once()
        call_args = presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        assert invalid_gof_id == given_gof_id

    def test_with_invalid_gof_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = \
            InvalidGoFIds(given_gof_ids)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gof_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_gof_ids.call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        assert invalid_gof_ids == given_gof_ids

    def test_with_invalid_gofs_to_task_template(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_task_template_id = "template_0"
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidGoFsOfTaskTemplate(given_gof_ids,
                                                     given_task_template_id)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_gofs_given_to_a_task_template \
                .call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        invalid_gofs_template_id = error_object.task_template_id
        assert invalid_gof_ids == given_gof_ids
        assert invalid_gofs_template_id == given_task_template_id

    def test_with_invalid_field_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_ids = ["field_0", "field_1", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFieldIds(given_field_ids)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_field_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_field_ids.call_args
        error_object = call_args[0][0]
        invalid_field_ids = error_object.field_ids
        assert invalid_field_ids == given_field_ids

    def test_with_duplicate_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_duplicate_field_ids = ["field_0", "field_0"]
        given_field_ids = given_duplicate_field_ids + ["field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = DuplicateFieldIdsToGoF(given_gof_id,
                                                  given_duplicate_field_ids)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_duplicate_field_ids_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_field_ids_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_duplicate_field_ids_to_a_gof.call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_duplicate_field_ids

    def test_with_invalid_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_field_ids = ["field_0", "field_0", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFieldsOfGoF(given_gof_id, given_field_ids)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_fields_given_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_fields_given_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_invalid_fields_given_to_a_gof \
            .call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_field_ids

    def test_with_user_who_does_not_have_write_permission_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_created_by_id = "user_0"
        given_gof_id = "gof_0"
        given_required_user_roles = ["role_1", "role_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(size=1,
                                                          gof_id=given_gof_id)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos, created_by_id=given_created_by_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsGoFWritablePermission

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserNeedsGoFWritablePermission(
            given_created_by_id, given_gof_id, given_required_user_roles)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_user_needs_gof_writable_permission.return_value \
            = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_gof_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_gof_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_gof_id = error_object.gof_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_gof_id == given_gof_id
        assert required_roles == given_required_user_roles

    def test_with_user_who_does_not_have_write_permission_to_a_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_created_by_id = "user_0"
        given_required_user_roles = ["role_1", "role_2"]
        given_field_id = "field_0"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos, created_by_id=given_created_by_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserNeedsFieldWritablePermission(
            given_created_by_id, given_field_id, given_required_user_roles)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_user_needs_field_writable_permission \
            .return_value \
            = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_field_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_field_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_field_id = error_object.field_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_field_id == given_field_id
        assert required_roles == given_required_user_roles

    def test_with_unfilled_gofs_which_are_required_and_user_permitted(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_display_names = ["gof_display_name_1", "gof_display_name_2"]
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserDidNotFillRequiredGoFs(given_gof_display_names)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_user_did_not_fill_required_gofs.return_value \
            = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_did_not_fill_required_gofs \
            .assert_called_once()
        call_args = presenter_mock.raise_user_did_not_fill_required_gofs \
            .call_args
        error_object = call_args[0][0]
        gof_display_names = error_object.gof_display_names
        assert gof_display_names == given_gof_display_names

    def test_with_unfilled_fields_which_are_required_and_user_permitted(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_unfilled_field_dtos = FieldIdWithFieldDisplayNameDTOFactory()
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields
        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserDidNotFillRequiredFields(
            given_unfilled_field_dtos)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_user_did_not_fill_required_fields.return_value \
            = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_did_not_fill_required_fields \
            .assert_called_once()
        call_args = presenter_mock.raise_user_did_not_fill_required_fields \
            .call_args
        error_object = call_args[0][0]
        unfilled_field_dtos = error_object.unfilled_field_dtos
        assert unfilled_field_dtos == given_unfilled_field_dtos

    def test_with_empty_response_to_a_required_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = ""
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = EmptyValueForRequiredField(given_field_id)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_phone_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_phone_number_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        assert invalid_field_id == given_field_id

    def test_with_invalid_response_to_a_phone_number_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "890808"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidPhoneNumberValue(given_field_id,
                                                   given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_phone_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_phone_number_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_email_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "sljlsjls@gmail"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidEmailFieldValue(given_field_id,
                                                  given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_email_address \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_email_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_email_address \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_url_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidURLValue(given_field_id,
                                           given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_url_address \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_url_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_url_address \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_weak_password_response_to_a_password_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "weak password"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = NotAStrongPassword(given_field_id,
                                              given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_weak_password \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_weak_password \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_weak_password \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_number_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidNumberValue(given_field_id,
                                              given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_number_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_number_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_float_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two point five"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFloatValue(given_field_id,
                                             given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_float_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_float_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_float_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_dropdown_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidValueForDropdownField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_dropdown_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_dropdown_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_dropdown_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_dropdown_choices = error_object.valid_values

        assert invalid_field_id == given_field_id
        assert valid_dropdown_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_name_to_a_gof_selector_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["gof selector name 1", "gof selector name 2"]
        given_field_response = '["gof selector name 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectNameInGoFSelectorField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_name_in_gof_selector \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_gof_selector_choices = error_object.valid_gof_selector_names

        assert invalid_field_id == given_field_id
        assert valid_gof_selector_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_radio_group_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectRadioGroupChoice(
            given_field_id, given_field_response, valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_choice_in_radio_group_field \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_radio_group_choices = error_object.valid_radio_group_options

        assert invalid_field_id == given_field_id
        assert valid_radio_group_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_check_box_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_checkbox_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_checkbox_options_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectCheckBoxOptionsSelected(
            given_field_id, invalid_checkbox_options_selected, valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_checkbox_group_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_check_box_response = error_object.invalid_checkbox_options
        valid_check_box_choices = error_object.valid_check_box_options

        assert invalid_field_id == given_field_id
        assert invalid_check_box_response == invalid_checkbox_options_selected
        assert valid_check_box_choices == valid_choices

    def test_with_invalid_option_to_a_multi_select_options_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_options_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectMultiSelectOptionsSelected(
            given_field_id, invalid_multi_select_options_selected,
            valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_options_response = \
            error_object.invalid_multi_select_options
        valid_multi_select_options = error_object.valid_multi_select_options

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_options_response == \
               invalid_multi_select_options_selected
        assert valid_multi_select_options == valid_choices

    def test_with_invalid_option_to_a_multi_select_label_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_labels_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_labels_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectMultiSelectLabelsSelected(
            given_field_id, invalid_multi_select_labels_selected, valid_choices
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_labels_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_labels_response = \
            error_object.invalid_multi_select_labels
        valid_multi_select_labels = error_object.valid_multi_select_labels

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_labels_response == \
               invalid_multi_select_labels_selected
        assert valid_multi_select_labels == valid_choices

    def test_with_invalid_date_format_to_a_date_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        from ib_tasks.constants.config import DATE_FORMAT
        expected_format = DATE_FORMAT
        given_field_response = "05-04-2020"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidDateFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_date_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_date_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_date_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_time_format_to_a_time_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        given_field_response = "2:30 PM"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidTimeFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_time_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_time_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_time_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_url_to_a_image_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid image url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidUrlForImage(given_field_id,
                                              given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_image_url.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_image_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_image_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_image_url = error_object.image_url

        assert invalid_field_id == given_field_id
        assert given_field_response == invalid_image_url

    def test_with_invalid_image_format_to_a_image_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid image format url"
        given_format = ".svg"
        allowed_formats = [".png", ".jpeg"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidImageFormat(given_field_id, given_format,
                                              allowed_formats)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_image_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_image_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_image_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_invalid_url_to_a_file_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid file url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidUrlForFile(given_field_id,
                                             given_field_response)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_invalid_file_url \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_file_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_file_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_file_url = error_object.file_url

        assert invalid_field_id == given_field_id
        assert invalid_file_url == given_field_response

    def test_with_invalid_file_format_to_a_file_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid file format url"
        given_format = ".zip"
        allowed_formats = [".pdf", ".xls"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFileFormat(given_field_id, given_format,
                                             allowed_formats)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_file_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_file_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_file_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_empty_stage_ids_list(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock,
            get_filtered_tasks_overview_for_user_mock
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        expected_existing_gofs = [
            GoFIdWithSameGoFOrderDTOFactory(
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        create_task_storage_mock \
            .get_gofs_details_of_task.return_value \
            = expected_existing_gofs
        field_ids = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            for field_values_dto in gof_fields_dto.field_values_dtos:
                field_ids.append(field_values_dto.field_id)
        task_gof_ids = [0, 0, 1, 1]
        expected_existing_fields = FieldIdWithTaskGoFIdDTOFactory.build_batch(
            size=len(field_ids), field_id=factory.Iterator(field_ids),
            task_gof_id=factory.Iterator(task_gof_ids)
        )
        create_task_storage_mock \
            .get_field_id_with_task_gof_id_dtos \
            .return_value = expected_existing_fields
        gof_ids = [gof.gof_id for gof in expected_existing_gofs]
        same_gof_orders = [gof.same_gof_order for gof in
                           expected_existing_gofs]
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=len(gof_ids), task_gof_id=factory.Iterator([0, 1]),
            gof_id=factory.Iterator(gof_ids),
            same_gof_order=factory.Iterator(same_gof_orders)
        )
        create_task_storage_mock.update_task_gofs.return_value = \
            expected_task_gof_details_dtos
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsListEmptyException
        get_filtered_tasks_overview_for_user_mock.side_effect = \
            StageIdsListEmptyException
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_stage_ids_list_empty_exception.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_stage_ids_list_empty_exception \
            .assert_called_once()

    def test_with_invalid_stage_ids_list(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock,
            get_filtered_tasks_overview_for_user_mock
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        expected_existing_gofs = [
            GoFIdWithSameGoFOrderDTOFactory(
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        create_task_storage_mock \
            .get_gofs_details_of_task.return_value \
            = expected_existing_gofs
        field_ids = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            for field_values_dto in gof_fields_dto.field_values_dtos:
                field_ids.append(field_values_dto.field_id)
        task_gof_ids = [0, 0, 1, 1]
        expected_existing_fields = FieldIdWithTaskGoFIdDTOFactory.build_batch(
            size=len(field_ids), field_id=factory.Iterator(field_ids),
            task_gof_id=factory.Iterator(task_gof_ids)
        )
        create_task_storage_mock \
            .get_field_id_with_task_gof_id_dtos \
            .return_value = expected_existing_fields
        gof_ids = [gof.gof_id for gof in expected_existing_gofs]
        same_gof_orders = [gof.same_gof_order for gof in
                           expected_existing_gofs]
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=len(gof_ids), task_gof_id=factory.Iterator([0, 1]),
            gof_id=factory.Iterator(gof_ids),
            same_gof_order=factory.Iterator(same_gof_orders)
        )
        create_task_storage_mock.update_task_gofs.return_value = \
            expected_task_gof_details_dtos
        stage_ids = ["stage_1", "stage_2"]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        get_filtered_tasks_overview_for_user_mock.side_effect = \
            InvalidStageIdsListException(stage_ids)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.raise_invalid_stage_ids_list_exception.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_ids_list_exception \
            .assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_ids_list_exception \
            .call_args
        error_object = call_args[0][0]
        invalid_stage_ids = error_object.invalid_stage_ids
        assert invalid_stage_ids == stage_ids

    def test_with_valid_task_details_updates_task(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock,
            get_filtered_tasks_overview_for_user_mock
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        expected_existing_gofs = [
            GoFIdWithSameGoFOrderDTOFactory(
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        create_task_storage_mock \
            .get_gofs_details_of_task.return_value \
            = expected_existing_gofs
        field_ids = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            for field_values_dto in gof_fields_dto.field_values_dtos:
                field_ids.append(field_values_dto.field_id)
        task_gof_ids = [0, 0, 1, 1]
        expected_existing_fields = FieldIdWithTaskGoFIdDTOFactory.build_batch(
            size=len(field_ids), field_id=factory.Iterator(field_ids),
            task_gof_id=factory.Iterator(task_gof_ids)
        )
        create_task_storage_mock \
            .get_field_id_with_task_gof_id_dtos \
            .return_value = expected_existing_fields
        expected_task_gof_dtos_for_updation = [
            TaskGoFWithTaskIdDTOFactory(
                task_id=task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        gof_ids = [gof.gof_id for gof in expected_existing_gofs]
        same_gof_orders = [gof.same_gof_order for gof in
                           expected_existing_gofs]
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=len(gof_ids), task_gof_id=factory.Iterator([0, 1]),
            gof_id=factory.Iterator(gof_ids),
            same_gof_order=factory.Iterator(same_gof_orders)
        )
        create_task_storage_mock.update_task_gofs.return_value = \
            expected_task_gof_details_dtos
        task_gof_ids = [0, 0, 1, 1]
        expected_task_gof_field_dtos = TaskGoFFieldDTOFactory.build_batch(
            size=4, task_gof_id=factory.Iterator(task_gof_ids))
        expected_task_gof_field_dtos_for_updation = \
            expected_task_gof_field_dtos
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        update_task_dto_with_task_db_id = UpdateTaskDTOFactory(
            task_id=task_id, created_by_id=task_dto.created_by_id,
            title=task_dto.title,
            description=task_dto.description,
            start_datetime=task_dto.start_datetime,
            due_datetime=task_dto.due_datetime,
            priority=task_dto.priority,
            stage_assignee=task_dto.stage_assignee,
            gof_fields_dtos=task_dto.gof_fields_dtos
        )
        create_task_storage_mock.update_task \
            .assert_called_once_with(task_dto=update_task_dto_with_task_db_id)
        create_task_storage_mock \
            .get_gofs_details_of_task \
            .assert_called_once_with(task_id)
        create_task_storage_mock.update_task_gofs(
            expected_task_gof_dtos_for_updation)
        create_task_storage_mock.update_task_gof_fields \
            .assert_called_once_with(
            expected_task_gof_field_dtos_for_updation)

    def test_with_invalid_permission_for_assignee_to_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        stage_assignees = [
            StageAssigneeDTOFactory(
                db_stage_id=task_dto.stage_assignee.stage_id,
                assignee_id=task_dto.stage_assignee.assignee_id,
                team_id=task_dto.stage_assignee.team_id
            )
        ]
        expected_task_stage_assignee_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_id, stage_assignees=stage_assignees)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        given_invalid_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        update_task_stage_assignees_mock.side_effect = \
            StageIdsWithInvalidPermissionForAssignee(
                given_invalid_stage_ids)
        presenter_mock \
            .raise_invalid_stage_assignees \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        update_task_stage_assignees_mock.assert_called_once_with(
            expected_task_stage_assignee_dto)
        presenter_mock \
            .raise_invalid_stage_assignees \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_stage_assignees \
            .call_args
        error_object = call_args[0][0]
        invalid_stage_ids = error_object.invalid_stage_ids
        assert invalid_stage_ids == given_invalid_stage_ids

    def test_with_valid_permission_for_assignee_to_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, action_storage_mock,
            task_stage_storage_mock, task_template_storage_mock,
            presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock,
            get_filtered_tasks_overview_for_user_mock
    ):
        # Arrange
        task_dto = UpdateTaskWithTaskDisplayIdDTOFactory()
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock,
            action_storage=action_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            task_template_storage=task_template_storage_mock
        )
        presenter_mock.get_update_task_response.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
