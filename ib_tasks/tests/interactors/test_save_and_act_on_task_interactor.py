import datetime

import mock
import pytest

from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF
from ib_tasks.interactors.create_or_update_task.save_and_act_on_task import \
    SaveAndActOnATaskInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    SaveAndActOnTaskWithTaskDisplayIdDTOFactory, GoFFieldsDTOFactory, \
    FieldValuesDTOFactory


class TestSaveAndActOnATaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        SaveAndActOnTaskWithTaskDisplayIdDTOFactory.reset_sequence()

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
            .action_storage_interface import ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces \
            .save_and_act_on_task_presenter_interface import \
            SaveAndActOnATaskPresenterInterface
        return mock.create_autospec(SaveAndActOnATaskPresenterInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return mock.create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def update_task_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".update_task_interactor.UpdateTaskInteractor.update_task"
        return mocker.patch(path)

    @pytest.fixture
    def user_action_on_task_mock(self, mocker):
        path = "ib_tasks.interactors.user_action_on_task_interactor" \
               ".UserActionOnTaskInteractor.user_action_on_task"
        return mocker.patch(path)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    def test_with_invalid_action_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object
    ):
        # Arrange
        given_action_id = 1
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            action_id=given_action_id)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        storage_mock.validate_action.side_effect = InvalidActionException(
            given_action_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_action_id.return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        storage_mock.validate_action.assert_called_once_with(given_action_id)
        presenter_mock.raise_invalid_action_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_action_id.call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == given_action_id

    def test_with_invalid_task_display_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_task_display_id = "task_1"
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        update_task_mock.side_effect = InvalidTaskDisplayId(
            given_task_display_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_task_display_id.return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        task_storage_mock.check_is_valid_task_display_id \
            .assert_called_once_with(
            task_display_id=given_task_display_id)
        presenter_mock.raise_invalid_task_display_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_display_id.call_args
        error_object = call_args[0][0]
        invalid_task_display_id = error_object.task_display_id
        assert invalid_task_display_id == given_task_display_id

    def test_with_invalid_task_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_task_display_id = 1
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskException
        update_task_mock.side_effect = InvalidTaskException(
            given_task_display_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_task_id.return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_task_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_id.call_args
        error_object = call_args[0][0]
        invalid_task_id = error_object.task_id
        assert invalid_task_id == given_task_display_id

    def test_with_invalid_stage_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_task_display_id = 1
        given_stage_id = 2
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            task_display_id=given_task_display_id,
            stage_assignee__stage_id=given_stage_id)

        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
        update_task_mock.side_effect = InvalidStageId(
            given_stage_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_stage_id.return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_id.call_args
        error_object = call_args[0][0]
        invalid_stage_id = error_object.stage_id
        assert invalid_stage_id == given_stage_id

    def test_with_invalid_due_time_format(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_due_time = "12-00-00"
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            due_time=given_due_time)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            InvalidDueTimeFormat
        update_task_mock.side_effect = InvalidDueTimeFormat(given_due_time)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_due_time_format.return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_due_time_format.assert_called_once()
        call_args = presenter_mock.raise_invalid_due_time_format.call_args
        error_object = call_args[0][0]
        invalid_due_time = error_object.due_time
        assert invalid_due_time == given_due_time

    def test_with_start_date_is_ahead_of_due_date(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_start_date = datetime.date(2020, 9, 1)
        given_due_date = datetime.date(2020, 8, 1)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            start_date=given_start_date, due_date=given_due_date)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateIsAheadOfDueDate
        update_task_mock.side_effect = StartDateIsAheadOfDueDate(
            given_start_date, given_due_date)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_start_date_is_ahead_of_due_date.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_is_ahead_of_due_date \
            .assert_called_once()
        call_args = presenter_mock.raise_start_date_is_ahead_of_due_date \
            .call_args
        error_object = call_args[0][0]
        invalid_start_date = error_object.given_start_date
        invalid_due_date = error_object.given_due_date
        assert invalid_start_date == given_start_date
        assert invalid_due_date == given_due_date

    def test_with_expired_due_time_for_today(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_due_time = "12-00-00"
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            due_time=given_due_time)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueTimeHasExpiredForToday
        update_task_mock.side_effect = DueTimeHasExpiredForToday(
            given_due_time)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_due_time_has_expired_for_today.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_time_has_expired_for_today \
            .assert_called_once()
        call_args = presenter_mock.raise_due_time_has_expired_for_today \
            .call_args
        error_object = call_args[0][0]
        invalid_due_time = error_object.due_time
        assert invalid_due_time == given_due_time

    def test_with_duplicate_same_gof_order(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_same_gof_order = 1
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=given_gof_id, same_gof_order=given_same_gof_order)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        update_task_mock.side_effect = DuplicateSameGoFOrderForAGoF(
            given_gof_id, [given_same_gof_order])
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_gof_ids = ["gof_1", "gof_2"]
        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        update_task_mock.side_effect = InvalidGoFIds(given_gof_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_gof_ids.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gof_ids \
            .assert_called_once()
        call_args = presenter_mock.raise_invalid_gof_ids \
            .call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        assert invalid_gof_ids == given_gof_ids

    def test_with_invalid_field_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_field_ids = ["field_1", "field_2"]
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        update_task_mock.side_effect = InvalidFieldIds(given_field_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_field_ids.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_field_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_field_ids.call_args
        error_object = call_args[0][0]
        invalid_field_ids = error_object.field_ids
        assert invalid_field_ids == given_field_ids

    def test_with_invalid_gofs_to_task_template(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_task_template_id = "task_template_1"
        given_gof_ids = ["gof_1", "gof_2"]
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate
        update_task_mock.side_effect = InvalidGoFsOfTaskTemplate(
            given_gof_ids, given_task_template_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_gofs_given_to_a_task_template \
                .call_args
        error_object = call_args[0][0]
        task_template_id = error_object.task_template_id
        invalid_gof_ids = error_object.gof_ids
        assert task_template_id == given_task_template_id
        assert invalid_gof_ids == given_gof_ids

    def test_with_duplicate_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_gof_id = "gof_1"
        given_field_ids = ["field_1", "field_2"]
        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF
        update_task_mock.side_effect = DuplicateFieldIdsToGoF(
            given_gof_id, given_field_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_duplicate_field_ids_to_a_gof \
            .return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_field_ids_to_a_gof \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_duplicate_field_ids_to_a_gof \
                .call_args
        error_object = call_args[0][0]
        gof_id = error_object.gof_id
        duplicate_field_ids = error_object.field_ids
        assert gof_id == given_gof_id
        assert duplicate_field_ids == given_field_ids

    def test_with_invalid_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_gof_id = "gof_1"
        given_field_ids = ["field_1", "field_2"]
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF
        update_task_mock.side_effect = InvalidFieldsOfGoF(
            given_gof_id, given_field_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_fields_given_to_a_gof \
            .return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_fields_given_to_a_gof \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_fields_given_to_a_gof \
                .call_args
        error_object = call_args[0][0]
        gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert gof_id == given_gof_id
        assert invalid_field_ids == given_field_ids

    def test_with_user_who_does_not_have_write_permission_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_user_id = "user_1"
        given_gof_id = "gof_1"
        given_required_roles = ["role_1", "role2"]
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsGoFWritablePermission
        update_task_mock.side_effect = UserNeedsGoFWritablePermission(
            given_user_id, given_gof_id, given_required_roles)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_user_needs_gof_writable_permission \
            .return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_gof_writable_permission \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_user_needs_gof_writable_permission \
                .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        gof_id = error_object.gof_id
        required_roles = error_object.required_roles

        assert user_id == given_user_id
        assert gof_id == given_gof_id
        assert required_roles == given_required_roles

    def test_with_user_who_does_not_have_write_permission_to_a_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        given_user_id = "user_1"
        given_field_id = "field_1"
        given_required_roles = ["role_1", "role2"]
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission
        update_task_mock.side_effect = UserNeedsFieldWritablePermission(
            given_user_id, given_field_id, given_required_roles)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_user_needs_field_writable_permission \
            .return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_field_writable_permission \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_user_needs_field_writable_permission \
                .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        field_id = error_object.field_id
        required_roles = error_object.required_roles

        assert user_id == given_user_id
        assert field_id == given_field_id
        assert required_roles == given_required_roles

    def test_with_empty_response_to_a_required_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = ""
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField
        update_task_mock \
            .side_effect = EmptyValueForRequiredField(given_field_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_empty_value_in_required_field \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_empty_value_in_required_field \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_empty_value_in_required_field \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        assert invalid_field_id == given_field_id

    def test_with_invalid_response_to_a_phone_number_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "890808"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        update_task_mock \
            .side_effect = InvalidPhoneNumberValue(given_field_id,
                                                   given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_phone_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_phone_number_value \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "sljlsjls@gmail"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        update_task_mock \
            .side_effect = InvalidEmailFieldValue(given_field_id,
                                                  given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_email_address \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_email_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_email_address \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        update_task_mock \
            .side_effect = InvalidURLValue(given_field_id,
                                           given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_url_address \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_url_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_url_address \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "weak password"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        update_task_mock \
            .side_effect = NotAStrongPassword(given_field_id,
                                              given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_weak_password \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_weak_password \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_weak_password \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        update_task_mock \
            .side_effect = InvalidNumberValue(given_field_id,
                                              given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_number_value \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_number_value \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two point five"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        update_task_mock \
            .side_effect = InvalidFloatValue(given_field_id,
                                             given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_float_value \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_float_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_float_value \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        update_task_mock \
            .side_effect = InvalidValueForDropdownField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_dropdown_value \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_invalid_dropdown_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_exception_for_invalid_dropdown_value \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        update_task_mock \
            .side_effect = IncorrectNameInGoFSelectorField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_name_in_gof_selector_field_value \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_name_in_gof_selector_field_value \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_name_in_gof_selector_field_value \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice
        update_task_mock \
            .side_effect = IncorrectRadioGroupChoice(
            given_field_id, given_field_response, valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_choice_in_radio_group_field \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_choice_in_radio_group_field \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_choice_in_radio_group_field \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected
        update_task_mock \
            .side_effect = IncorrectCheckBoxOptionsSelected(
            given_field_id, invalid_checkbox_options_selected, valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_checkbox_group_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_checkbox_group_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_checkbox_group_options_selected \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        update_task_mock \
            .side_effect = IncorrectMultiSelectOptionsSelected(
            given_field_id, invalid_multi_select_options_selected,
            valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_multi_select_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_multi_select_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_multi_select_options_selected \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected
        update_task_mock \
            .side_effect = IncorrectMultiSelectLabelsSelected(
            given_field_id, invalid_multi_select_labels_selected, valid_choices
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_multi_select_labels_selected \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_multi_select_labels_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_multi_select_labels_selected \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat
        update_task_mock \
            .side_effect = InvalidDateFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_date_format \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_date_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_date_format \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        update_task_mock \
            .side_effect = InvalidTimeFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_time_format \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_time_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_time_format \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid image url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        update_task_mock \
            .side_effect = InvalidUrlForImage(given_field_id,
                                              given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_exception_for_invalid_image_url.return_value = \
            mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_image_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_image_url \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat
        update_task_mock \
            .side_effect = InvalidImageFormat(given_field_id, given_format,
                                              allowed_formats)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_not_acceptable_image_format \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_not_acceptable_image_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_not_acceptable_image_format \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid file url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile
        update_task_mock \
            .side_effect = InvalidUrlForFile(given_field_id,
                                             given_field_response)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_file_url \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_file_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_file_url \
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
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock
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
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat
        update_task_mock \
            .side_effect = InvalidFileFormat(given_field_id, given_format,
                                             allowed_formats)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_not_acceptable_file_format \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_not_acceptable_file_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_not_acceptable_file_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_invalid_user_permission_to_given_action(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock,
            user_action_on_task_mock
    ):
        # Arrange
        given_action_id = 1
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            action_id=given_action_id)

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserActionPermissionDenied
        user_action_on_task_mock.side_effect = UserActionPermissionDenied(
            given_action_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_user_action_permission_denied \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_user_action_permission_denied \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_user_action_permission_denied.call_args
        error_object = call_args.kwargs['error_obj']
        action_id = error_object.action_id

        assert action_id == given_action_id

    def test_with_invalid_present_stage_action(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock,
            user_action_on_task_mock
    ):
        # Arrange
        given_action_id = 1
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory(
            action_id=given_action_id)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        user_action_on_task_mock.side_effect = InvalidPresentStageAction(
            given_action_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_exception_for_invalid_present_stage_actions \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_exception_for_invalid_present_stage_actions \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_exception_for_invalid_present_stage_actions.call_args
        error_object = call_args[0][0]
        action_id = error_object.action_id
        assert action_id == given_action_id

    def test_with_invalid_assignee_permission_for_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object, update_task_mock,
            user_action_on_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskWithTaskDisplayIdDTOFactory()
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        given_stage_ids = [1, 2, 3]
        user_action_on_task_mock.side_effect = \
            StageIdsWithInvalidPermissionForAssignee(given_stage_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock \
            .raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .return_value = mock_object

        # Act
        response = interactor.save_and_act_on_task_wrapper(presenter_mock,
                                                           task_dto)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .call_args
        error_object = call_args[0][0]
        stage_ids = error_object.invalid_stage_ids

        assert stage_ids == given_stage_ids
