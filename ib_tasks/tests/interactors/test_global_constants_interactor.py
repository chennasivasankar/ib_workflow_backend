import mock
import pytest

from ib_tasks.interactors.global_constants_dtos import \
    GlobalConstantsWithTemplateIdDTO
from ib_tasks.interactors.global_constants_interactor import \
    GlobalConstantsInteractor
from ib_tasks.tests.factories.interactor_dtos import GlobalConstantsDTOFactory


class TestGlobalConstantsInteractor:
    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        task_template_storage = mock.create_autospec(
            TaskTemplateStorageInterface)
        return task_template_storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory
        GlobalConstantsDTOFactory.reset_sequence()

    def test_with_invalid_value_for_template_id_field_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = " "

        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        expected_exception_message = INVALID_VALUE_FOR_TEMPLATE_ID

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_value_for_constant_name_field_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"

        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_CONSTANT_NAME
        expected_exception_message = INVALID_VALUE_FOR_CONSTANT_NAME

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name=" "
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_value_for_value_field_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        invalid_value = -1
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_VALUE
        expected_exception_message = \
            INVALID_VALUE_FOR_VALUE.format(invalid_value)

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, value=invalid_value
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_duplicate_constant_names_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_CONSTANT_NAMES
        expected_exception_message = \
            DUPLICATE_CONSTANT_NAMES.format(['Constant_1'])

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name="Constant_1"
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.constants_custom_exceptions import \
            DuplicateConstantNames

        # Assert
        with pytest.raises(DuplicateConstantNames) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_id_raises_exception(self,
                                                       task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        from ib_tasks.constants.exception_messages import \
            TEMPLATE_DOES_NOT_EXISTS
        expected_exception_message = \
            TEMPLATE_DOES_NOT_EXISTS.format(template_id)
        task_template_storage_mock.check_is_template_exists.return_value = \
            False

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.task_custom_exceptions import \
            TemplateDoesNotExists

        # Assert
        with pytest.raises(TemplateDoesNotExists) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_create_global_constants_with_valid_data(self,
                                                     task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"

        task_template_storage_mock.check_is_template_exists.return_value = True
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )

        # Act
        global_constants_interactor \
            .create_global_constants_to_template_wrapper(
            global_constants_with_template_id_dto
            =global_constants_with_template_id_dto
        )

        # Assert
        task_template_storage_mock.create_global_constants_to_template. \
            assert_called_once_with(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )

    def test_when_existing_constants_not_in_given_data_creates_constants_and_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        existing_global_constants_names = ["Constant_4"]

        from ib_tasks.constants.exception_messages import \
            EXISTING_GLOBAL_CONSTANT_NAMES_NOT_IN_GIVEN_DATA
        expected_exception_message = \
            EXISTING_GLOBAL_CONSTANT_NAMES_NOT_IN_GIVEN_DATA.format(
                existing_global_constants_names
            )

        task_template_storage_mock.check_is_template_exists.return_value = True

        global_constants_dtos = \
            GlobalConstantsDTOFactory.create_batch(size=2)
        task_template_storage_mock. \
            get_constant_names_of_existing_global_constants_of_template. \
            return_value = existing_global_constants_names

        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )
        from ib_tasks.exceptions.constants_custom_exceptions import \
            ExistingGlobalConstantNamesNotInGivenData

        # Assert
        with pytest.raises(ExistingGlobalConstantNamesNotInGivenData) as err:
            global_constants_interactor \
                .create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto
                =global_constants_with_template_id_dto
            )
        task_template_storage_mock.create_global_constants_to_template. \
            assert_called_once_with(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
        assert err.value.args[0] == expected_exception_message

    def test_when_unique_constant_name_but_different_configuration_updates_global_constant(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        existing_global_constants_names = ["Constant_1", "Constant_2"]
        task_template_storage_mock.check_is_template_exists.return_value = True

        global_constants_dtos = \
            GlobalConstantsDTOFactory.create_batch(size=2)
        task_template_storage_mock. \
            get_constant_names_of_existing_global_constants_of_template. \
            return_value = existing_global_constants_names

        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_interactor = GlobalConstantsInteractor(
            task_template_storage=task_template_storage_mock
        )

        # Assert
        global_constants_interactor \
            .create_global_constants_to_template_wrapper(
            global_constants_with_template_id_dto
            =global_constants_with_template_id_dto
        )
        task_template_storage_mock.update_global_constants_to_template. \
            assert_called_once_with(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
