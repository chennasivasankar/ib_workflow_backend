import pytest
import mock
from ib_tasks.interactors.global_constants_interactor import \
    GlobalConstantsInteractor
from ib_tasks.interactors.dtos import GlobalConstantsWithTemplateIdDTO
from ib_tasks.tests.factories.interactor_dtos import GlobalConstantsDTOFactory


class TestGlobalConstantsInteractor:
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            GlobalConstantsDTOFactory
        GlobalConstantsDTOFactory.reset_sequence()

    def test_with_invalid_value_for_template_id_field_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = " "
        expected_exception_message = "Invalid value for field: template_id"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_value_for_constant_name_field_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = "Invalid value for field: constant_name"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name=" "
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_value_for_value_field_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = "Invalid value for field: value"

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, value=-1
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_duplicate_constant_names_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = \
            "Given duplicate constant names ['Constant_1']"
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name="Constant_1"
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import \
            DuplicateConstantNames

        # Assert
        with pytest.raises(DuplicateConstantNames) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_id_raises_exception(self,
                                                       task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = \
            "The template with template id: FIN_PR, does not exists"
        task_storage_mock.check_is_template_exists.return_value = False

        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import \
            TemplateDoesNotExists

        # Assert
        with pytest.raises(TemplateDoesNotExists) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_create_global_constants_with_valid_data(self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"

        task_storage_mock.check_is_template_exists.return_value = True
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )

        # Act
        global_constants_interactor.create_global_constants_to_template_wrapper(
            global_constants_with_template_id_dto=global_constants_with_template_id_dto
        )

        #Assert
        task_storage_mock.create_global_constants_to_template.\
            assert_called_once_with(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

    def test_when_existing_constants_not_in_given_data_creates_constants_and_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = \
            "Existing constants with constant names: ['Constant_4'] of template not in given data"
        task_storage_mock.check_is_template_exists.return_value = True
        existing_global_constants_names = ["Constant_4"]
        global_constants_dtos = \
            GlobalConstantsDTOFactory.create_batch(size=2)
        task_storage_mock.\
            get_constant_names_of_existing_global_constants_of_template.\
            return_value = existing_global_constants_names

        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGlobalConstantNamesNotInGivenData

        # Assert
        with pytest.raises(ExistingGlobalConstantNamesNotInGivenData) as err:
            global_constants_interactor.create_global_constants_to_template_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        task_storage_mock.create_global_constants_to_template.\
            assert_called_once_with(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
        )
        assert err.value.args[0] == expected_exception_message
