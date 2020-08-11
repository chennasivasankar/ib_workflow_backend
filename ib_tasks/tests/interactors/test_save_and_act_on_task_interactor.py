import datetime

import mock
import pytest

from ib_tasks.interactors.create_or_update_task.save_and_act_on_task import \
    SaveAndActOnATaskInteractor
from ib_tasks.tests.factories.interactor_dtos import SaveAndActOnTaskDTOFactory


class TestSaveAndActOnATaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        SaveAndActOnTaskDTOFactory.reset_sequence()

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
            action_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_action_id = 1
        task_dto = SaveAndActOnTaskDTOFactory(action_id=given_action_id)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        storage_mock.validate_action.side_effect = InvalidActionException(
            given_action_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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

    def test_with_invalid_task_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_task_id = 1
        task_dto = SaveAndActOnTaskDTOFactory(task_id=given_task_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskException
        update_task_mock.side_effect = InvalidTaskException(given_task_id)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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
        assert invalid_task_id == given_task_id

    def test_with_invalid_due_time_format(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_due_time = "12-00-00"
        task_dto = SaveAndActOnTaskDTOFactory(due_time=given_due_time)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            InvalidDueTimeFormat
        update_task_mock.side_effect = InvalidDueTimeFormat(given_due_time)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_start_date = datetime.date(2020, 9, 1)
        given_due_date = datetime.date(2020, 8, 1)
        task_dto = SaveAndActOnTaskDTOFactory(
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
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        given_due_time = "12-00-00"
        task_dto = SaveAndActOnTaskDTOFactory(due_time=given_due_time)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueTimeHasExpiredForToday
        update_task_mock.side_effect = DueTimeHasExpiredForToday(
            given_due_time)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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

    def test_with_invalid_gof_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
        given_gof_ids = ["gof_1", "gof_2"]
        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        update_task_mock.side_effect = InvalidGoFIds(given_gof_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
        given_field_ids = ["field_1", "field_2"]
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        update_task_mock.side_effect = InvalidFieldIds(given_field_ids)
        interactor = SaveAndActOnATaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
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
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
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
            elastic_storage=elastic_storage_mock)
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
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
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
            elastic_storage=elastic_storage_mock)
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

    def test_with_invalid_user_permission_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
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
            elastic_storage=elastic_storage_mock)
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

    def test_with_invalid_user_permission_to_a_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock,
            action_storage_mock, presenter_mock, mock_object, update_task_mock
    ):
        # Arrange
        task_dto = SaveAndActOnTaskDTOFactory()
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
            elastic_storage=elastic_storage_mock)
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
