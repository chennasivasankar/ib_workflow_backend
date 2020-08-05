import mock
import pytest

from ib_tasks.interactors.create_task_template_interactor \
    import CreateTaskTemplateInteractor
from ib_tasks.interactors.task_template_dtos import CreateTaskTemplateDTO


class TestTaskTemplateInteractor:
    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        task_template_storage = mock.create_autospec(
            TaskTemplateStorageInterface)
        return task_template_storage

    def test_with_invalid_template_name_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = " "

        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_NAME
        expected_message = INVALID_VALUE_FOR_TEMPLATE_NAME

        from ib_tasks.interactors.create_task_template_interactor \
            import CreateTaskTemplateInteractor
        task_template_interactor = CreateTaskTemplateInteractor(
            task_template_storage=task_template_storage_mock
        )

        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_message

    def test_with_invalid_template_id_raises_exception(
            self, task_template_storage_mock):
        # Arrange
        template_id = "  "
        template_name = "Request Payment"

        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        expected_message = INVALID_VALUE_FOR_TEMPLATE_ID

        from ib_tasks.interactors.create_task_template_interactor \
            import CreateTaskTemplateInteractor
        task_template_interactor = CreateTaskTemplateInteractor(
            task_template_storage=task_template_storage_mock
        )
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_message

    def test_create_task_template_with_valid_data(self,
                                                  task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        task_template_interactor = CreateTaskTemplateInteractor(
            task_template_storage=task_template_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = \
            False

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_template_storage_mock.create_task_template \
            .assert_called_once_with(
            template_id=template_id, template_name=template_name
        )

    def test_with_existing_template_id_but_different_name_updates_template(
            self, task_template_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name
        )
        task_template_interactor = CreateTaskTemplateInteractor(
            task_template_storage=task_template_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = True

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_template_storage_mock.update_task_template \
            .assert_called_once_with(
            template_id=template_id, template_name=template_name
        )
