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

    @pytest.mark.parametrize("template_id", ["", " ", 1, True, 1.0])
    def test_with_invalid_value_for_template_id_field_raises_exception(
            self, task_storage_mock, template_id):
        # Arrange
        template_id = template_id
        expected_exception_message = "Invalid value for field: template_id"
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    @pytest.mark.parametrize("constant_name", ["", " ", 1, True, 1.0])
    def test_with_invalid_value_for_constant_name_field_raises_exception(
            self, task_storage_mock, constant_name):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = "Invalid value for field: constant_name"

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, constant_name=constant_name
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    @pytest.mark.parametrize("value", ["", " ", 1, True, 1.0])
    def test_with_invalid_value_for_value_field_raises_exception(
            self, task_storage_mock, value):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = "Invalid value for field: value"

        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(
            size=2, value=value
        )
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            global_constants_interactor.create_global_constants_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_id_raises_exception(self,
                                                       task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        expected_exception_message = \
            "Template does not exists for the given template_id: FIN_PR"
        task_storage_mock.check_is_template_exists.return_value = False
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )
        from ib_tasks.exceptions.custom_exceptions import \
            TemplateDoesNotExists

        # Assert
        with pytest.raises(TemplateDoesNotExists) as err:
            global_constants_interactor.create_global_constants_wrapper(
                global_constants_with_template_id_dto=global_constants_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_create_global_constants_with_valid_data(self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"

        task_storage_mock.check_is_template_exists.return_value = True
        global_constants_interactor = GlobalConstantsInteractor(
            task_storage=task_storage_mock
        )
        global_constants_dtos = GlobalConstantsDTOFactory.create_batch(size=2)
        global_constants_with_template_id_dto = \
            GlobalConstantsWithTemplateIdDTO(
                template_id=template_id,
                global_constants_dtos=global_constants_dtos
            )

        # Act
        global_constants_interactor.create_global_constants_wrapper(
            global_constants_with_template_id_dto=global_constants_with_template_id_dto
        )

        #Assert
        task_storage_mock.create_global_constants_to_template.\
            assert_called_once_with(
            template_id=template_id,
            global_constants_dtos=global_constants_dtos
        )
