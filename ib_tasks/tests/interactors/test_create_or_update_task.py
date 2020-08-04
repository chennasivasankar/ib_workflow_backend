from typing import List, Optional

import pytest
import factory

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.interactors.create_or_update_task import \
    CreateOrUpdateTaskInteractor
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskGoFDetailsDTO
from ib_tasks.tests.common_fixtures.interactors import \
    mock_user_action_on_task_method
from ib_tasks.tests.factories.interactor_dtos import TaskDTOFactory, \
    GoFFieldsDTOFactory, FieldValuesDTOFactory
from ib_tasks.tests.factories.storage_dtos import FieldCompleteDetailsDTOFactory, \
    TaskGoFWithTaskIdDTOFactory, TaskGoFDetailsDTOFactory, \
    TaskGoFFieldDTOFactory


class TestCreateOrUpdateTask:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskDTOFactory.reset_sequence(1)
        GoFFieldsDTOFactory.reset_sequence(1)
        FieldValuesDTOFactory.reset_sequence(1)
        FieldCompleteDetailsDTOFactory.reset_sequence(1)
        TaskGoFWithTaskIdDTOFactory.reset_sequence(1)
        TaskGoFDetailsDTOFactory.reset_sequence(1)
        TaskGoFFieldDTOFactory.reset_sequence(1)

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        from mock import create_autospec
        task_storage_mock = create_autospec(TaskStorageInterface)
        return task_storage_mock

    @pytest.fixture
    def create_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
            import CreateOrUpdateTaskStorageInterface
        from mock import create_autospec
        return create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        from mock import create_autospec
        storage_mock = create_autospec(StorageInterface)
        return storage_mock

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
            FieldsStorageInterface
        from mock import create_autospec
        return create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        from mock import create_autospec
        return create_autospec(StageStorageInterface)

    @pytest.fixture
    def act_on_task_presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.presenter_interface import \
            PresenterInterface
        from mock import create_autospec
        return create_autospec(PresenterInterface)

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

    def test_create_or_update_task_with_invalid_gof_ids_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):

        # Arrange
        task_dto = TaskDTOFactory()
        task_storage_mock.check_is_template_exists.return_value = True
        task_storage_mock.get_existing_gof_ids.return_value = ["GOF_ID-5"]
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.create_or_update_task_wrapper(
            presenter_mock, task_dto, act_on_task_presenter_mock
        )

        # Assert
        assert response == mock_object
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.assert_called_once_with(
            gof_ids=gof_ids
        )
        presenter_mock.raise_exception_for_invalid_gof_ids.assert_called_once()

    def test_create_or_update_task_with_invalid_field_ids_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        task_dto = TaskDTOFactory()
        task_storage_mock.check_is_template_exists.return_value = True
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = ["FIELD_ID-10"]
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )
        presenter_mock.raise_exception_for_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        field_ids = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            field_ids += [
                field_value_dto.field_id
                for field_value_dto in gof_fields_dto.field_values_dtos
            ]
        task_storage_mock.get_existing_field_ids.assert_called_once_with(
            field_ids)
        presenter_mock.raise_exception_for_invalid_field_ids.assert_called_once()

    def test_create_or_update_task_with_invalid_name_in_gof_selector_value_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="company"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values='[{"name": "individual", "gof_ids": ["gof_0"]}]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = \
            field_details_dtos
        presenter_mock.raise_exception_for_invalid_name_in_gof_selector_field_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_name_in_gof_selector_field_value.assert_called_once()

    @pytest.mark.parametrize("phone_number",
                             ["phone_number", "989  89", "97979sjsljs"])
    def test_create_or_update_task_with_invalid_phone_number_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, phone_number, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=phone_number
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_phone_number_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(
            presenter_mock, task_dto, act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_phone_number_value.assert_called_once()

    @pytest.mark.parametrize("email",
                             ["email", "gmail.com"])
    def test_create_or_update_task_with_invalid_email_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, email, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=email
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_email_address.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(
            presenter_mock, task_dto, act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_email_address.assert_called_once()

    @pytest.mark.parametrize("url_address",
                             ["google", "www.google.com", "google.in"])
    def test_create_or_update_task_with_invalid_url_address_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, url_address, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=url_address
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_url_address.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_url_address.assert_called_once()

    @pytest.mark.parametrize("password",
                             ["password", "8798", "Pas788", "7979passI"])
    def test_create_or_update_task_with_weak_password_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, password, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=password
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_weak_password.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_weak_password.assert_called_once()

    @pytest.mark.parametrize("number",
                             ["password", "87()", "7+8", "90!2"])
    def test_create_or_update_task_with_number_value_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, number, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=number
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_number_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_number_value.assert_called_once()

    @pytest.mark.parametrize("float_value",
                             ["float_value", "87.2*3", "7+8.67"])
    def test_create_or_update_task_with_invalid_float_value_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, float_value, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=float_value
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_float_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_float_value.assert_called_once()

    def test_create_or_update_task_with_invalid_dropdown_value_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="Hyderbad"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.DROPDOWN.value,
            field_values='["Kurnool", "Vizag"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_dropdown_value.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_dropdown_value.assert_called_once()

    def test_create_or_update_task_with_invalid_radio_group_choice_value_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="internal"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.RADIO_GROUP.value,
            field_values='["male", "female"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_choice_in_radio_group_field.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_choice_in_radio_group_field.assert_called_once()

    def test_create_or_update_task_with_invalid_checkbox_options_selected_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response='["testcases", "interactors"]'
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.CHECKBOX_GROUP.value,
            field_values='["storages", "presenters"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_checkbox_group_options_selected.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_checkbox_group_options_selected.assert_called_once()

    def test_create_or_update_task_with_invalid_multi_select_options_selected_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response='["testcases", "interactors"]'
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.MULTI_SELECT_FIELD.value,
            field_values='["storages", "presenters"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_multi_select_options_selected.return_value = mock_object

        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_multi_select_options_selected.assert_called_once()

    def test_create_or_update_task_with_invalid_multi_select_labels_selected_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response='["testcases", "interactors"]'
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.MULTI_SELECT_LABELS.value,
            field_values='["storages", "presenters"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_multi_select_labels_selected.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_multi_select_labels_selected.assert_called_once()

    @pytest.mark.parametrize("date_string", ["03-06-2020", "03/07/2020"])
    def test_create_or_update_task_with_invalid_date_format_date_string_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, date_string, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=date_string
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.DATE.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_date_format.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_date_format.assert_called_once()

    @pytest.mark.parametrize("time_string", ["12:30", "12:60:23"])
    def test_create_or_update_task_with_invalid_time_format_time_string_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, time_string, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response=time_string
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.TIME.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_time_format.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_time_format.assert_called_once()

    def test_create_or_update_task_with_invalid_image_url_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="www.google.com/"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats='[".jpeg", ".svg"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_image_url.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_image_url.assert_called_once()

    def test_create_or_update_task_with_valid_image_url_but_with_format_not_in_allowed_formats_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1,
            field_response="https://image.flaticon.com/icons/svg/1829/1829070.svg"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats='[".jpeg", ".png"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_not_acceptable_image_format.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_not_acceptable_image_format.assert_called_once()

    def test_create_or_update_task_with_invalid_file_url_raises_exception(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="www.google.com/"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.FILE_UPLOADER.value,
            allowed_formats='[".zip", ".tar"]'
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        presenter_mock.raise_exception_for_invalid_file_url.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        presenter_mock.raise_exception_for_invalid_file_url.assert_called_once()

    def test_create_or_update_task_with_invalid_task_task_tempalte_id_raises_exception(
            self, task_storage_mock, create_task_storage_mock, presenter_mock,
            mock_object,
            storage_mock, act_on_task_presenter_mock, field_storage_mock,
            stage_storage_mock
    ):

        # Arrange
        task_template_id = "TASK_TEMPLATE_ID-1"
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=1, field_response="text"
        )
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PLAIN_TEXT.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos, task_template_id=task_template_id
        )
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        task_storage_mock.check_is_template_exists.return_value = False
        presenter_mock.raise_exception_for_invalid_task_template_id.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        task_storage_mock.check_is_template_exists.assert_called_once_with(
            template_id=task_template_id
        )
        presenter_mock.raise_exception_for_invalid_task_template_id.assert_called_once()

    def test_create_or_update_task_with_valid_details_creates_task(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock,
            mocker, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(1)
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
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
        created_task_id = 1
        task_gof_details_dtos = TaskGoFDetailsDTOFactory.create_batch(1)
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        create_task_storage_mock.create_task_with_template_id.return_value = created_task_id
        create_task_storage_mock.create_task_gofs.return_value = task_gof_details_dtos
        presenter_mock.get_response_for_create_or_update_task.return_value = mock_object
        user_action_on_task_mock = mock_user_action_on_task_method(mocker,
                                                                   mock_object)
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        user_action_on_task_mock.assert_called_once()
        task_storage_mock.get_field_details_for_given_field_ids.assert_called_once_with(
            field_ids=field_ids
        )
        create_task_storage_mock.create_task_with_template_id.assert_called_once_with(
            task_dto.task_template_id, task_dto.created_by_id
        )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTOFactory(
                task_id=created_task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        create_task_storage_mock.create_task_gofs.assert_called_once_with(
            task_gof_dtos=task_gof_dtos
        )
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTOFactory(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in gof_fields_dto.field_values_dtos
            ]
        create_task_storage_mock.create_task_gof_fields.assert_called_once_with(
            task_gof_field_dtos
        )
        presenter_mock.get_response_for_create_or_update_task.assert_called_once()

    @staticmethod
    def _get_gof_id_for_field_in_task_gof_details(
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

    def test_create_or_update_task_with_invalid_task_id(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, field_storage_mock, stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(1)
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PLAIN_TEXT.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos, task_id=1
        )
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        create_task_storage_mock.is_valid_task_id.return_value = False
        presenter_mock.raise_exception_for_invalid_task_id.return_value = mock_object
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        create_task_storage_mock.is_valid_task_id.assert_called_once_with(1)
        presenter_mock.raise_exception_for_invalid_task_id.assert_called_once()

    def test_create_or_update_task_with_valid_task_id_updates_task(
            self, task_storage_mock, create_task_storage_mock,
            presenter_mock, mock_object, storage_mock,
            act_on_task_presenter_mock, mocker, field_storage_mock,
            stage_storage_mock
    ):
        # Arrange
        gof_field_values_dtos = FieldValuesDTOFactory.create_batch(1)
        field_ids = [
            gof_field_values_dto.field_id
            for gof_field_values_dto in gof_field_values_dtos
        ]
        field_details_dtos = FieldCompleteDetailsDTOFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids),
            field_type=FieldTypes.PLAIN_TEXT.value
        )
        gof_fields_dtos = GoFFieldsDTOFactory.create_batch(
            size=1, field_values_dtos=gof_field_values_dtos
        )
        task_dto = TaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos, task_id=1
        )
        gof_ids = [
            gof_fields_dto.gof_id
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        task_gof_details_dtos = TaskGoFDetailsDTOFactory.create_batch(1)
        task_storage_mock.get_existing_gof_ids.return_value = gof_ids
        task_storage_mock.get_existing_field_ids.return_value = field_ids
        task_storage_mock.get_field_details_for_given_field_ids.return_value = field_details_dtos
        create_task_storage_mock.is_valid_task_id.return_value = True
        create_task_storage_mock.update_task_gofs.return_value = task_gof_details_dtos
        create_task_storage_mock.get_gof_ids_with_same_gof_order_related_to_a_task.return_value = \
            gof_ids
        create_task_storage_mock.get_field_ids_with_task_gof_id_related_to_given_task.return_value = \
            field_ids
        presenter_mock.get_response_for_create_or_update_task.return_value = mock_object
        user_action_on_task_mock = mock_user_action_on_task_method(mocker,
                                                                   mock_object)
        interactor = CreateOrUpdateTaskInteractor(
            task_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock
        )

        # Act
        response = interactor.create_or_update_task_wrapper(presenter_mock,
                                                            task_dto,
                                                            act_on_task_presenter_mock)

        # Assert
        assert response == mock_object
        user_action_on_task_mock.assert_called_once()
        task_gof_dtos = [
            TaskGoFWithTaskIdDTOFactory(
                task_id=1,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        create_task_storage_mock.update_task_gofs.assert_called_once_with(
            task_gof_dtos=task_gof_dtos
        )
        task_gof_field_dtos = []
        for gof_fields_dto in task_dto.gof_fields_dtos:
            task_gof_id = self._get_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTOFactory(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in gof_fields_dto.field_values_dtos
            ]
        create_task_storage_mock.update_task_gof_fields.assert_called_once_with(
            task_gof_field_dtos
        )
        presenter_mock.get_response_for_create_or_update_task.assert_called_once()
