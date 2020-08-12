import datetime
from typing import List, Optional

import factory
import freezegun
import mock
import pytest

from ib_tasks.documents.elastic_task import ElasticFieldDTO, ElasticTaskDTO
from ib_tasks.interactors.create_or_update_task.update_task_interactor import \
    UpdateTaskInteractor
from ib_tasks.interactors.stages_dtos import StageAssigneeDTO, \
    TaskIdWithStageAssigneesDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.task_dtos import UpdateTaskDTO, FieldValuesDTO
from ib_tasks.tests.factories.interactor_dtos import FieldValuesDTOFactory, \
    GoFFieldsDTOFactory, UpdateTaskDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    GoFIdWithSameGoFOrderDTOFactory, FieldIdWithTaskGoFIdDTOFactory, \
    TaskGoFDetailsDTOFactory


class TestUpdateTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldValuesDTOFactory.reset_sequence()
        GoFFieldsDTOFactory.reset_sequence()
        UpdateTaskDTOFactory.reset_sequence()
        GoFIdWithSameGoFOrderDTOFactory.reset_sequence()
        FieldIdWithTaskGoFIdDTOFactory.reset_sequence()
        TaskGoFDetailsDTOFactory.reset_sequence()

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

    def test_with_invalid_task_id(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_task_id = "task_1"
        task_dto = UpdateTaskDTOFactory(task_id=given_task_id)
        create_task_storage_mock.is_valid_task_id.return_value = False
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_invalid_task_id.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        create_task_storage_mock.is_valid_task_id.assert_called_once_with(
            given_task_id)
        presenter_mock.raise_invalid_task_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_id.call_args
        error_object = call_args[0][0]
        invalid_task_id = error_object.task_id
        assert invalid_task_id == given_task_id

    def test_with_invalid_due_time_format(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_due_time = "12-12-12"
        task_id = "task_1"
        task_dto = UpdateTaskDTOFactory(task_id=task_id,
                                        due_time=given_due_time)
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = \
            "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_invalid_due_time_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_due_time_format.assert_called_once()
        call_args = presenter_mock.raise_invalid_due_time_format.call_args
        error_object = call_args[0][0]
        invalid_due_time = error_object.due_time
        assert invalid_due_time == given_due_time

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_date(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_due_date = datetime.date(2020, 9, 1)
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        task_dto = UpdateTaskDTOFactory(due_date=given_due_date)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_due_date_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_has_expired.assert_called_once()
        call_args = presenter_mock.raise_due_date_has_expired.call_args
        error_object = call_args[0][0]
        invalid_due_date = error_object.due_date
        assert invalid_due_date == given_due_date

    def test_with_start_date_ahead_of_due_date(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_start_date = datetime.date(2020, 9, 9)
        given_due_date = datetime.date(2020, 9, 1)
        task_dto = UpdateTaskDTOFactory(start_date=given_start_date,
                                        due_date=given_due_date)
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
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
        assert invalid_start_date == given_start_date
        assert invalid_due_date == given_due_date

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_time_for_today(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_start_date = datetime.date(2020, 9, 1)
        given_due_date = datetime.date(2020, 9, 9)
        given_due_time = "12:00:00"
        task_dto = UpdateTaskDTOFactory(start_date=given_start_date,
                                        due_date=given_due_date,
                                        due_time=given_due_time)
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_due_time_has_expired_for_today \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_task_template_id = "template_0"
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_ids = ["field_0", "field_1", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_field_ids = ["field_0", "field_0", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_created_by_id = "user_0"
        given_gof_id = "gof_0"
        given_required_user_roles = ["role_1", "role_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(size=1,
                                                          gof_id=given_gof_id)
        task_dto = UpdateTaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos, created_by_id=given_created_by_id)
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
            elastic_storage=elastic_storage_mock
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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos, created_by_id=given_created_by_id)
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
            elastic_storage=elastic_storage_mock
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

    def test_with_empty_response_to_a_required_field(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_empty_value_in_required_field \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_email_address \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_url_address \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_weak_password \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_number_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_float_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_dropdown_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_name_in_gof_selector_field_value \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_choice_in_radio_group_field \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_checkbox_group_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_multi_select_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_multi_select_labels_selected \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_date_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_time_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_image_url.return_value = \
            mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_not_acceptable_image_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_invalid_file_url \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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
            elastic_storage_mock, presenter_mock, mock_object,
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
        task_dto = UpdateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
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
            elastic_storage=elastic_storage_mock
        )
        presenter_mock \
            .raise_exception_for_not_acceptable_file_format \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

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

    def test_with_valid_task_details_updates_task(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock
    ):
        # Arrange
        task_dto = UpdateTaskDTOFactory()
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
            .get_gof_ids_with_same_gof_order_related_to_a_task.return_value \
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
            .get_field_ids_with_task_gof_id_related_to_given_task \
            .return_value = expected_existing_fields
        expected_task_gof_dtos_for_updation = [
            TaskGoFWithTaskIdDTO(
                task_id=task_dto.task_id,
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
        expected_task_gof_field_dtos_for_updation = \
            self._prepare_task_gof_fields_dtos(task_dto,
                                               expected_task_gof_details_dtos)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        create_task_storage_mock.update_task_with_given_task_details \
            .assert_called_once_with(task_dto=task_dto)
        elastic_storage_mock.update_task.assert_called_once_with(
            task_dto=self._get_elastic_task_dto(task_dto))
        create_task_storage_mock \
            .get_gof_ids_with_same_gof_order_related_to_a_task \
            .assert_called_once_with(
            task_dto.task_id)
        create_task_storage_mock.update_task_gofs(
            expected_task_gof_dtos_for_updation)
        create_task_storage_mock.update_task_gof_fields \
            .assert_called_once_with(
            expected_task_gof_field_dtos_for_updation)

    def _get_elastic_task_dto(self, task_dto: UpdateTaskDTO):

        fields_dto = self._get_fields_dto(task_dto)
        elastic_task_dto = ElasticTaskDTO(
            template_id=None,
            task_id=task_dto.task_id,
            title=task_dto.title,
            fields=fields_dto
        )
        return elastic_task_dto

    def _get_fields_dto(
            self, task_dto: UpdateTaskDTO) -> List[ElasticFieldDTO]:

        fields_dto = []
        gof_fields_dtos = task_dto.gof_fields_dtos
        for gof_fields_dto in gof_fields_dtos:
            for field_value_dto in gof_fields_dto.field_values_dtos:
                fields_dto.append(self._get_elastic_field_dto(field_value_dto))

        return fields_dto

    @staticmethod
    def _get_elastic_field_dto(field_dto: FieldValuesDTO) -> ElasticFieldDTO:
        return ElasticFieldDTO(
            field_id=field_dto.field_id,
            value=field_dto.field_response
        )

    def _prepare_task_gof_fields_dtos(
            self, task_dto: UpdateTaskDTO,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_task_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos)
            if task_gof_id is not None:
                task_gof_field_dtos += [
                    TaskGoFFieldDTO(
                        field_id=field_values_dto.field_id,
                        field_response=field_values_dto.field_response,
                        task_gof_id=task_gof_id
                    )
                    for field_values_dto in gof_fields_dto.field_values_dtos
                ]
        return task_gof_field_dtos

    @staticmethod
    def _get_task_gof_id_for_field_in_task_gof_details(
            gof_id: str, same_gof_order: int,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> Optional[int]:
        for task_gof_details_dto in task_gof_details_dtos:
            gof_matched = (
                    task_gof_details_dto.gof_id == gof_id and
                    task_gof_details_dto.same_gof_order == same_gof_order
            )
            if gof_matched:
                return task_gof_details_dto.task_gof_id
        return

    def test_with_invalid_permission_for_assignee_to_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock
    ):
        # Arrange
        task_dto = UpdateTaskDTOFactory()
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        stage_assignees = [
            StageAssigneeDTO(
                db_stage_id=task_dto.stage_assignee.stage_id,
                assignee_id=task_dto.stage_assignee.assignee_id
            )
        ]
        expected_task_stage_assignee_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_dto.task_id, stage_assignees=stage_assignees)
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        given_invalid_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        update_task_stage_assignees_mock.side_effect = \
            StageIdsWithInvalidPermissionForAssignee(
                given_invalid_stage_ids)
        presenter_mock \
            .raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        update_task_stage_assignees_mock.assert_called_once_with(
            expected_task_stage_assignee_dto)
        presenter_mock \
            .raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception \
            .call_args
        error_object = call_args[0][0]
        invalid_stage_ids = error_object.invalid_stage_ids
        assert invalid_stage_ids == given_invalid_stage_ids

    def test_with_valid_permission_for_assignee_to_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            perform_base_validations_for_template_gofs_and_fields_mock,
            update_task_stage_assignees_mock
    ):
        # Arrange
        task_dto = UpdateTaskDTOFactory()
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.get_template_id_for_given_task.return_value \
            = "template_1"
        interactor = UpdateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            elastic_storage=elastic_storage_mock
        )
        presenter_mock.get_update_task_response.return_value = mock_object

        # Act
        response = interactor.update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
