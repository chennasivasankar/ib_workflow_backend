
import pytest
import factory

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.tests.factories.interactor_dtos import (
    TaskDTOFactory, GoFFieldsDTOFactory, FieldValuesDTOFactory
)
from ib_tasks.interactors.create_or_update_task import \
    CreateOrUpdateTaskInteractor
from ib_tasks.tests.factories.storage_dtos import FieldTypeDTOFactory


class TestCreateOrUpdateTask:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskDTOFactory.reset_sequence(1)
        GoFFieldsDTOFactory.reset_sequence(1)
        FieldValuesDTOFactory.reset_sequence(1)
        FieldTypeDTOFactory.reset_sequence(1)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from mock import create_autospec
        storage_mock = create_autospec(TaskStorageInterface)
        return storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.create_or_update_task_presenter \
            import CreateOrUpdateTaskPresenterInterface
        from mock import create_autospec
        presenter_mock = create_autospec(CreateOrUpdateTaskPresenterInterface)
        return presenter_mock

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        return Mock()

    def test_create_or_update_task_with_duplicate_gof_ids_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=2, gof_id="GOF_ID-1"
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        presenter_mock.raise_exception_for_duplicate_gof_ids.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_duplicate_gof_ids.assert_called_once()

    def test_create_or_update_task_with_duplicate_field_ids_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=2, field_id="FIELD_ID-1"
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )

        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        presenter_mock.raise_exception_for_duplicate_field_ids.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        presenter_mock.raise_exception_for_duplicate_field_ids.assert_called_once()


    def test_create_or_update_task_with_invalid_task_task_tempalte_id_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):

        # Arrange
        task_template_id = "TASK_TEMPLATE_ID-1"
        task_dto = TaskDTOFactory(task_template_id=task_template_id)
        storage_mock.check_is_template_exists.return_value = False
        interactor = CreateOrUpdateTaskInteractor(storage_mock)
        presenter_mock.raise_exception_for_invalid_task_template_id.return_value = mock_object

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        storage_mock.check_is_template_exists.assert_called_once_with(
            template_id=task_template_id
        )
        presenter_mock.raise_exception_for_invalid_task_template_id.assert_called_once()

    def test_create_or_update_task_with_invalid_gof_ids_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):

        # Arrange
        task_dto = TaskDTOFactory()
        storage_mock.check_is_template_exists.return_value = True
        storage_mock.get_existing_gof_ids.return_value = ["GOF_ID-5"]
        interactor = CreateOrUpdateTaskInteractor(storage_mock)
        presenter_mock.raise_exception_for_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        storage_mock.get_existing_gof_ids.assert_called_once_with(
            gof_ids=gof_ids
        )
        presenter_mock.raise_exception_for_invalid_gof_ids.assert_called_once()

    def test_create_or_update_task_with_invalid_field_ids_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        task_dto = TaskDTOFactory()
        storage_mock.check_is_template_exists.return_value = True
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        storage_mock.get_existing_gof_ids.return_value = gof_ids
        storage_mock.get_existing_field_ids.return_value = ["FIELD_ID-10"]
        interactor = CreateOrUpdateTaskInteractor(storage_mock)
        presenter_mock.raise_exception_for_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        field_ids = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        storage_mock.get_existing_field_ids.assert_called_once_with(field_ids)
        presenter_mock.raise_exception_for_invalid_field_ids.assert_called_once()


    def test_create_or_update_task_with_empty_value_for_plain_text_field_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=2, field_value="  "
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldTypeDTOFactory.create_batch(
            size=2, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PLAIN_TEXT.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        storage_mock.get_existing_gof_ids.return_value = gof_ids
        storage_mock.get_existing_field_ids.return_value = field_ids
        storage_mock.get_field_types_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_empty_value_in_plain_text_field.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_types_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_empty_value_in_plain_text_field.assert_called_once()
