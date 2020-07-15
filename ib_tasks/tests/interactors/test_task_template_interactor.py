import pytest
import mock
from ib_tasks.interactors.task_template_interactor \
    import TaskTemplateInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    GoFIDAndOrderDTOFactory
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
        GoFIDAndOrderDTOFactory.reset_sequence()

    def test_with_invalid_order_for_gof_ids_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )

        expected_exception_message = "Invalid value for field: order"
        gof_dtos = \
            GoFIDAndOrderDTOFactory.create_batch(size=1, order=-2)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    @pytest.mark.parametrize("template_name", ["", " ", 1, bool, 1.0])
    def test_with_invalid_template_name_raises_exception(
            self, task_storage_mock, template_name):
        # Arrange
        template_id = "FIN_PR"
        template_name = template_name

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        expected_exception_message = "Invalid value for field: template_name"
        gof_dtos = \
            GoFIDAndOrderDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    @pytest.mark.parametrize("template_id", ["", " ", 1, bool, 1.0])
    def test_with_invalid_template_id_raises_exception(
            self, task_storage_mock, template_id):
        # Arrange
        template_id = template_id
        template_name = "Request Payment"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        expected_exception_message = "Invalid value for field: template_id"
        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    @pytest.mark.parametrize("gof_id", ["", " ", 1, bool, 1.0])
    def test_with_invalid_gof_id_raises_exception(
            self, task_storage_mock, gof_id):
        # Arrange
        template_id = "FIN"
        template_name = "Request Payment"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        expected_exception_message = "Invalid value for field: gof_id"
        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(size=1, gof_id="")
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_create_task_template_with_duplicate_gof_ids_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"
        expected_exception_message = \
            "Given duplicate gof ids ['PaymentRequestDetails']"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )

        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(
            size=2, gof_id="PaymentRequestDetails"
        )
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions \
            import DuplicateGoFIds

        # Assert
        with pytest.raises(DuplicateGoFIds) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_when_existing_gof_ids_of_template_not_in_given_data_raises_exception(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        from ib_tasks.interactors.task_template_interactor \
            import TaskTemplateInteractor
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )

        task_storage_mock.check_is_template_exists.return_value = True
        task_storage_mock. \
            get_existing_gof_ids_of_template.return_value = ["GoF_5"]
        expected_exception_message = \
            "Existing gof ids: ['GoF_5'] of template not in given gof ids: ['GoF_1']"

        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        from ib_tasks.exceptions.custom_exceptions import \
            ExistingGoFNotInGivenGoF

        # Assert
        with pytest.raises(ExistingGoFNotInGivenGoF) as err:
            task_template_interactor.create_task_template_wrapper(
                create_task_template_dto=create_task_template_dto
            )
        task_storage_mock. \
            get_existing_gof_ids_of_template.assert_called_once_with(
                template_id=template_id
            )
        assert err.value.args[0] == expected_exception_message

    def test_create_task_template_with_valid_data(self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"
        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(size=1)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        task_storage_mock.check_is_template_exists.return_value = False

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_storage_mock.create_task_template.assert_called_once_with(
            template_id=template_id, template_name=template_name
        )

    def test_create_task_template_with_existing_template_updates_template_gofs(
            self, task_storage_mock):
        # Arrange
        template_id = "FIN_PR"
        template_name = "Payment Request"

        gof_dtos = GoFIDAndOrderDTOFactory.create_batch(size=3)
        create_task_template_dto = CreateTaskTemplateDTO(
            template_id=template_id, template_name=template_name,
            gof_dtos=gof_dtos
        )
        task_template_interactor = TaskTemplateInteractor(
            task_storage=task_storage_mock
        )
        task_storage_mock.check_is_template_exists.return_value = True
        task_storage_mock.\
            get_existing_gof_ids_of_template.return_value = ["GoF_1"]
        from ib_tasks.interactors.dtos import GoFIDAndOrderDTO
        expected_gof_dtos_to_add_to_template = [
            GoFIDAndOrderDTO(gof_id='GoF_2', order=2),
            GoFIDAndOrderDTO(gof_id='GoF_3', order=3)
        ]

        # Act
        task_template_interactor.create_task_template_wrapper(
            create_task_template_dto=create_task_template_dto
        )

        # Assert
        task_storage_mock.add_gofs_to_task_template.assert_called_once_with(
            template_id=template_id,
            gof_id_and_order_dtos=expected_gof_dtos_to_add_to_template
        )
