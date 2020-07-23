
import pytest
import factory

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.create_or_update_task import \
    CreateOrUpdateTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import TaskDTOFactory, \
    GoFFieldsDTOFactory, FieldValuesDTOFactory
from ib_tasks.tests.factories.storage_dtos import FieldDetailsDTOFactory


class TestCreateOrUpdateTask:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskDTOFactory.reset_sequence(1)
        GoFFieldsDTOFactory.reset_sequence(1)
        FieldValuesDTOFactory.reset_sequence(1)
        FieldDetailsDTOFactory.reset_sequence(1)

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

    def test_create_or_update_task_with_invalid_gof_ids_in_gof_selector_value_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value="GOF_ID-10"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.GOF_SELECTOR.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        storage_mock.get_existing_gof_ids.return_value = ["GOF_ID-1", "GOF_ID-2"]
        storage_mock.get_existing_field_ids.return_value = field_ids
        storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_gof_ids_in_gof_selector_field_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_gof_ids_in_gof_selector_field_value.assert_called_once()


    def test_create_or_update_task_with_empty_value_for_plain_text_field_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value="  "
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_empty_value_in_plain_text_field.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_empty_value_in_plain_text_field.assert_called_once()


    @pytest.mark.parametrize("phone_number", ["phone_number", "989  89", "97979sjsljs"])
    def test_create_or_update_task_with_invalid_phone_number_raises_exception(
            self, storage_mock, presenter_mock, mock_object, phone_number
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=phone_number
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PHONE_NUMBER.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_phone_number_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock, task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_phone_number_value.assert_called_once()

    @pytest.mark.parametrize("email",
                             ["email", "email  @gmail.com", "gmail.com"])
    def test_create_or_update_task_with_invalid_email_raises_exception(
            self, storage_mock, presenter_mock, mock_object, email
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=email
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.EMAIL.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_email_address.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_email_address.assert_called_once()

    @pytest.mark.parametrize("url_address",
                             ["google", "www.google.com", "google.in"])
    def test_create_or_update_task_with_invalid_url_address_raises_exception(
            self, storage_mock, presenter_mock, mock_object, url_address
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=url_address
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.URL.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_url_address.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_url_address.assert_called_once()

    @pytest.mark.parametrize("password",
                             ["password", "8798", "", "Pas788", "7979passI"])
    def test_create_or_update_task_with_weak_password_raises_exception(
            self, storage_mock, presenter_mock, mock_object, password
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=password
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PASSWORD.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_weak_password.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_weak_password.assert_called_once()

    @pytest.mark.parametrize("number",
                             ["password", "87()", "", "7+8", "90!2"])
    def test_create_or_update_task_with_number_value_raises_exception(
            self, storage_mock, presenter_mock, mock_object, number
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=number
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.NUMBER.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_number_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_number_value.assert_called_once()

    @pytest.mark.parametrize("float_value",
                             ["float_value", "87.2*3", "7+8.67"])
    def test_create_or_update_task_with_invalid_float_value_raises_exception(
            self, storage_mock, presenter_mock, mock_object, float_value
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value=float_value
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.FLOAT.value
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_float_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_float_value.assert_called_once()

    def test_create_or_update_task_with_invalid_dropdown_value_raises_exception(
            self, storage_mock, presenter_mock, mock_object
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_value="Hyderbad"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_type_dtos = FieldDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.DROPDOWN.value,
            field_values=["Kurnool", "Vizag"]
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
        storage_mock.get_field_details_for_given_field_ids.return_value = field_type_dtos
        presenter_mock.raise_exception_for_invalid_dropdown_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(storage_mock)

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto)

        # Assert
        assert response == mock_object
        storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_dropdown_value.assert_called_once()