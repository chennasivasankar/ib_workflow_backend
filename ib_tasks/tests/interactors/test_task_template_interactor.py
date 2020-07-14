import pytest
import mock
from ib_tasks.interactors.task_template_interactor \
    import TaskTemplateInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    GroupOfFieldsDTOFactory
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO


class TestTaskTemplateInteractor:
    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        task_storage = mock.create_autospec(TaskStorageInterface)
        return task_storage

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GroupOfFieldsDTOFactory.reset_sequence()

    def test_create_task_template_with_valid_data(self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        group_of_fields_dtos = GroupOfFieldsDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_storage_mock.create_task_template.assert_called_once_with(
            create_task_template_dto=create_task_template_dto
        )

    def test_create_task_template_with_existing_template_updates_template(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        group_of_fields_dtos = GroupOfFieldsDTOFactory.create_batch(size=3)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        task_storage_mock.get_task_template_name_if_exists.return_value = \
            "Payment Request"
        task_storage_mock.\
            get_existing_group_of_fields_of_template.return_value = ["GOF_1"]

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_storage_mock.update_task_template.assert_called_once_with(
            create_task_template_dto=create_task_template_dto
        )

    def test_create_task_template_with_duplicate_group_of_fields_ids_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"
        expected_exception_message = \
            "Given Duplicate group_of_fields_ids: ['PaymentRequestDetails']"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )

        group_of_fields_dtos = GroupOfFieldsDTOFactory.create_batch(
            size=2, group_of_fields_id="PaymentRequestDetails"
        )
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateGroupOfFields

        # Assert
        with pytest.raises(DuplicateGroupOfFields) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_existing_template_id_but_different_name_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        task_storage_mock.get_task_template_name_if_exists.return_value = \
            "Vendor"
        expected_exception_message = \
            "Template already exists! you have given different template name: Payment Request"

        group_of_fields_dtos = GroupOfFieldsDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import DifferentTemplateName

        # Assert
        with pytest.raises(DifferentTemplateName) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        task_storage_mock. \
            get_task_template_name_if_exists.assert_called_once_with(
                template_id=template_id
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_existing_group_of_fields_ids_not_in_given_data(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists
        task_storage_mock. \
            get_existing_group_of_fields_of_template.return_value = ["GOF_5"]
        expected_exception_message = \
            "Existing group of fields ids not in given group of fields ids: ['GOF_5']"

        group_of_fields_dtos = GroupOfFieldsDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGroupOfFieldsNotInGivenGroupOfFields

        # Assert
        with pytest.raises(
                ExistingGroupOfFieldsNotInGivenGroupOfFields
        ) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        task_storage_mock. \
            get_existing_group_of_fields_of_template.assert_called_once_with(
                template_id=template_id
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_order_for_group_of_fields_ids_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists
        task_storage_mock. \
            get_existing_group_of_fields_of_template.return_value = []
        expected_exception_message = \
            "Invalid Order: -2 for group_of_fields_id: GOF_1"

        group_of_fields_dtos = \
            GroupOfFieldsDTOFactory.create_batch(size=1, order=-2)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import InvalidOrder

        # Assert
        with pytest.raises(InvalidOrder) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_name_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = ""

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists
        task_storage_mock. \
            get_existing_group_of_fields_of_template.return_value = []
        expected_exception_message = "Invalid for field: template_name"

        group_of_fields_dtos = \
            GroupOfFieldsDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_id_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = ""
        template_name = "Request Payment"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists
        task_storage_mock. \
            get_existing_group_of_fields_of_template.return_value = []
        expected_exception_message = "Invalid for field: template_id"

        group_of_fields_dtos = \
            GroupOfFieldsDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_group_of_fields_id_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN"
        template_name = "Request Payment"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        from ib_tasks.exceptions.custom_exceptions import TemplateNotExists
        task_storage_mock.get_task_template_name_if_exists.side_effect = \
            TemplateNotExists
        task_storage_mock. \
            get_existing_group_of_fields_of_template.return_value = []
        expected_exception_message = "Invalid for field: group_of_fields_id"

        group_of_fields_dtos = \
            GroupOfFieldsDTOFactory.create_batch(
                size=1, group_of_fields_id=""
            )
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            group_of_fields_dtos=group_of_fields_dtos
        )

        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message
