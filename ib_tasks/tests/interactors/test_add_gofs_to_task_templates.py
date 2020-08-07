import mock
import pytest

from ib_tasks.interactors.add_gofs_to_template_interactor import \
    AddGoFsToTemplateInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    GoFWithOrderAndAddAnotherDTOFactory, GoFsWithTemplateIdDTOFactory


class TestAddGoFsToTaskTemplates:
    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        task_template_storage = mock.create_autospec(
            TaskTemplateStorageInterface)
        return task_template_storage

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFWithOrderAndAddAnotherDTOFactory.reset_sequence()
        GoFsWithTemplateIdDTOFactory.reset_sequence()

    def test_with_invalid_value_for_template_id_field_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange

        template_id = " "
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_TEMPLATE_ID
        expected_exception_message = \
            INVALID_VALUE_FOR_TEMPLATE_ID

        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            template_id=template_id
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_value_for_gof_id_field_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            INVALID_VALUE_FOR_GOF_IDS
        expected_exception_message = INVALID_VALUE_FOR_GOF_IDS

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, gof_id="  "
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos
        )
        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidValueForField

        # Assert
        with pytest.raises(InvalidValueForField) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_order_values_for_gof_ids_field_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            INVALID_ORDERS_FOR_GOFS
        expected_exception_message = \
            INVALID_ORDERS_FOR_GOFS.format(['gof_1', 'gof_2'])

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=-2
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            InvalidOrdersForGoFs

        # Assert
        with pytest.raises(InvalidOrdersForGoFs) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_duplicate_order_values_for_gof_ids_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_ORDER_VALUES_FOR_GOFS
        expected_exception_message = \
            DUPLICATE_ORDER_VALUES_FOR_GOFS.format([2])

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, order=2
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            DuplicateOrderValuesForGoFs

        # Assert
        with pytest.raises(DuplicateOrderValuesForGoFs) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_duplicate_gof_ids_raises_exception(self,
                                                     task_template_storage_mock,
                                                     gof_storage_mock):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            DUPLICATE_GOF_IDS
        expected_exception_message = \
            DUPLICATE_GOF_IDS.format(["gof_1"])

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2, gof_id="gof_1"
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.gofs_custom_exceptions import DuplicateGoFIds

        # Assert
        with pytest.raises(DuplicateGoFIds) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_template_id_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        invalid_template_id = "template_3"
        from ib_tasks.constants.exception_messages import \
            TEMPLATE_DOES_NOT_EXISTS
        expected_exception_message = \
            TEMPLATE_DOES_NOT_EXISTS.format(invalid_template_id)

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos, template_id=invalid_template_id
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = \
            False
        from ib_tasks.exceptions.task_custom_exceptions import \
            TemplateDoesNotExists

        # Assert
        with pytest.raises(TemplateDoesNotExists) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_with_invalid_gof_ids_raises_exception(self,
                                                   task_template_storage_mock,
                                                   gof_storage_mock):
        # Arrange
        template_id = "template_1"
        expected_invalid_gof_ids = ['gof_1']
        from ib_tasks.constants.exception_messages import \
            GOFS_DOES_NOT_EXIST
        expected_exception_message = \
            GOFS_DOES_NOT_EXIST.format(expected_invalid_gof_ids)

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(
            size=2
        )
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos, template_id=template_id
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = True
        task_template_storage_mock.get_existing_gof_ids_of_template \
            .return_value = []
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids \
            .return_value = \
            ['gof_2']
        from ib_tasks.exceptions.gofs_custom_exceptions import GofsDoesNotExist

        # Assert
        with pytest.raises(GofsDoesNotExist) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )
        assert err.value.args[0] == expected_exception_message

    def test_add_gofs_to_template_with_valid_data(self,
                                                  task_template_storage_mock,
                                                  gof_storage_mock):
        # Arrange
        template_id = "template_1"

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos, template_id=template_id
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = True
        task_template_storage_mock.get_existing_gof_ids_of_template \
            .return_value = []
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids \
            .return_value = \
            ['gof_1', 'gof_2']

        # Act
        interactor.add_gofs_to_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

        # Assert
        task_template_storage_mock.add_gofs_to_template \
            .assert_called_once_with(
            template_id=template_id, gof_dtos=gof_dtos
        )

    def test_when_gofs_already_exists_but_given_different_configuration_updates_gofs_to_template(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_1"

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos, template_id=template_id
        )

        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = True
        task_template_storage_mock.get_existing_gof_ids_of_template \
            .return_value = \
            ['gof_2']
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids \
            .return_value = \
            ['gof_1', 'gof_2']

        from ib_tasks.interactors.gofs_dtos import GoFWithOrderAndAddAnotherDTO
        expected_gof_dtos_to_update = [
            GoFWithOrderAndAddAnotherDTO(
                gof_id='gof_2', order=1, enable_add_another_gof=True
            )
        ]

        # Act
        interactor.add_gofs_to_template_wrapper(
            gofs_with_template_id_dto=gofs_with_template_id_dto
        )

        # Assert
        task_template_storage_mock.update_gofs_to_template \
            .assert_called_once_with(
            template_id=template_id, gof_dtos=expected_gof_dtos_to_update
        )

    def test_when_gofs_already_exists_but_not_given_in_present_configuraton_adds_gofs_and_raises_exception(
            self, task_template_storage_mock, gof_storage_mock):
        # Arrange
        template_id = "template_1"
        expected_existing_gof_ids_that_are_not_in_given_data = \
            ['gof_3', 'gof_4']
        from ib_tasks.constants.exception_messages import \
            EXISTING_GOFS_NOT_IN_GIVEN_DATA
        expected_exception_message = \
            EXISTING_GOFS_NOT_IN_GIVEN_DATA.format(
                expected_existing_gof_ids_that_are_not_in_given_data
            )

        gof_dtos = GoFWithOrderAndAddAnotherDTOFactory.create_batch(size=2)
        gofs_with_template_id_dto = GoFsWithTemplateIdDTOFactory(
            gof_dtos=gof_dtos, template_id=template_id
        )
        interactor = AddGoFsToTemplateInteractor(
            task_template_storage=task_template_storage_mock,
            gof_storage=gof_storage_mock
        )
        task_template_storage_mock.check_is_template_exists.return_value = True
        task_template_storage_mock.get_existing_gof_ids_of_template \
            .return_value = \
            expected_existing_gof_ids_that_are_not_in_given_data
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids \
            .return_value = \
            ['gof_1', 'gof_2']

        from ib_tasks.exceptions.gofs_custom_exceptions import \
            ExistingGoFsNotInGivenData

        # Assert
        with pytest.raises(ExistingGoFsNotInGivenData) as err:
            interactor.add_gofs_to_template_wrapper(
                gofs_with_template_id_dto=gofs_with_template_id_dto
            )

        assert err.value.args[0] == expected_exception_message
        task_template_storage_mock.add_gofs_to_template.assert_called_once_with(
            template_id=template_id, gof_dtos=gof_dtos
        )
