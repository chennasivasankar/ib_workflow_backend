import factory
import mock
import pytest

from ib_tasks.interactors.create_or_update_transition_checklist_template import \
    CreateOrUpdateTransitionChecklistTemplateInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory, \
    GoFFieldsDTOFactory, FieldValuesDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    TaskGoFWithTaskIdDTOFactory, \
    TaskGoFDetailsDTOFactory, TaskGoFFieldDTOFactory


class TestCreateTransitionChecklistInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory \
            .reset_sequence()
        GoFFieldsDTOFactory.reset_sequence()
        FieldValuesDTOFactory.reset_sequence()
        TaskGoFWithTaskIdDTOFactory.reset_sequence()
        TaskGoFDetailsDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()

    @pytest.fixture
    def create_or_update_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        return mock.create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture
    def template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def stage_action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import \
            ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import \
            TaskStorageInterface
        return mock.create_autospec(TaskStorageInterface)

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        return mock.create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces \
            .create_transition_checklist_presenter_interface import \
            CreateOrUpdateTransitionChecklistTemplatePresenterInterface
        return mock.create_autospec(
            CreateOrUpdateTransitionChecklistTemplatePresenterInterface)

    @pytest.fixture
    def perform_base_validations_for_template_gofs_and_fields_mock(self,
                                                                   mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".template_gofs_fields_base_validations" \
               ".TemplateGoFsFieldsBaseValidationsInteractor" \
               ".perform_base_validations_for_template_gofs_and_fields"
        return mocker.patch(path)

    def test_with_invalid_task_display_id(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        given_task_display_id = "task_1"
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                task_display_id=given_task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_task_display_id.return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        task_storage_mock.check_is_valid_task_display_id \
            .assert_called_once_with(given_task_display_id)
        presenter_mock.raise_invalid_task_display_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_display_id.call_args
        error_object = call_args[0][0]
        invalid_task_display_id = error_object.task_display_id
        assert invalid_task_display_id == given_task_display_id

    def test_with_invalid_task_id(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        given_task_display_id = "task_1"
        task_id = 1
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                task_display_id=given_task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            False
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_task_id.return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        create_or_update_task_storage_mock.is_valid_task_id \
            .assert_called_once_with(
            task_id)
        presenter_mock.raise_invalid_task_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_id.call_args
        error_object = call_args[0][0]
        invalid_task_id = error_object.task_id
        assert invalid_task_id == task_id

    def test_with_invalid_transition_checklist_template_id(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        given_task_display_id = "task_1"
        given_transition_checklist_template_id = "checklist_template_1"
        task_id = 1
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                task_display_id=given_task_display_id,
                transition_checklist_template_id
                =given_transition_checklist_template_id
            )
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTransitionChecklistTemplateId
        template_storage_mock.validate_transition_template_id.side_effect = \
            InvalidTransitionChecklistTemplateId(
                given_transition_checklist_template_id)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_transition_checklist_template_id \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        template_storage_mock.validate_transition_template_id \
            .assert_called_once_with(
            given_transition_checklist_template_id)
        presenter_mock.raise_invalid_transition_checklist_template_id \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_transition_checklist_template_id \
                .call_args
        error_object = call_args[0][0]
        invalid_transition_template_id = \
            error_object.transition_checklist_template_id
        assert invalid_transition_template_id == \
               given_transition_checklist_template_id

    def test_with_invalid_action_id(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        task_id = 1
        given_action_id = 2
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                action_id=given_action_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        stage_action_storage_mock.validate_action_id.side_effect = \
            InvalidActionException(given_action_id)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_action \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        stage_action_storage_mock.validate_action_id.assert_called_once_with(
            given_action_id)
        presenter_mock.raise_invalid_action.assert_called_once()
        call_args = presenter_mock.raise_invalid_action.call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == given_action_id

    def test_with_invalid_stage_id(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        task_id = 1
        given_stage_id = 2
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                stage_id=given_stage_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
        stage_action_storage_mock.validate_stage_id.side_effect = \
            InvalidStageId(given_stage_id)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_stage_id.return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        stage_action_storage_mock.validate_stage_id.assert_called_once_with(
            given_stage_id)
        presenter_mock.raise_invalid_stage_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_id.call_args
        error_object = call_args[0][0]
        invalid_stage_id = error_object.stage_id
        assert invalid_stage_id == given_stage_id

    def test_with_irrelevant_transition_template_for_given_stage_action(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        task_id = 1
        given_stage_id = 2
        given_action_id = 3
        given_transition_template_id = "transition_template_1"
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                stage_id=given_stage_id, action_id=given_action_id,
                transition_checklist_template_id=given_transition_template_id
            )
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        from ib_tasks.exceptions.stage_custom_exceptions import \
            TransitionTemplateIsNotRelatedToGivenStageAction
        stage_action_storage_mock \
            .validate_transition_template_id_is_related_to_given_stage_action. \
            side_effect = TransitionTemplateIsNotRelatedToGivenStageAction(
            stage_id=given_stage_id, action_id=given_action_id,
            transition_checklist_template_id=given_transition_template_id
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_transition_template_is_not_related_to_given_stage_action \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        stage_action_storage_mock \
            .validate_transition_template_id_is_related_to_given_stage_action. \
            assert_called_once_with(
            given_transition_template_id, given_action_id, given_stage_id
        )
        presenter_mock \
            .raise_transition_template_is_not_related_to_given_stage_action \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_transition_template_is_not_related_to_given_stage_action \
            .call_args
        error_object = call_args[0][0]
        stage_id = error_object.stage_id
        action_id = error_object.action_id
        transition_template_id = error_object.transition_checklist_template_id
        assert stage_id == given_stage_id
        assert action_id == given_action_id
        assert transition_template_id == given_transition_template_id

    def test_with_duplicate_same_gof_order_for_a_gof(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock
    ):
        # Arrange
        task_id = 1
        given_gof_id = "gof_1"
        given_same_gof_orders = [1]
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=2, gof_id=given_gof_id, same_gof_order=1)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_same_gof_order_for_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_same_gof_order_for_a_gof.assert_called_once()
        call_args = presenter_mock.raise_same_gof_order_for_a_gof.call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        same_gof_orders = error_object.same_gof_orders
        assert invalid_gof_id == given_gof_id
        assert same_gof_orders == given_same_gof_orders

    def test_with_invalid_gof_ids(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"
        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = \
            InvalidGoFIds(given_gof_ids)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gof_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_gof_ids.call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        assert invalid_gof_ids == given_gof_ids

    def test_with_invalid_gofs_to_task_template(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_task_template_id = "template_0"
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidGoFsOfTaskTemplate(given_gof_ids,
                                                     given_task_template_id)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_gofs_given_to_a_task_template \
                .call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        invalid_gofs_template_id = error_object.task_template_id
        assert invalid_gof_ids == given_gof_ids
        assert invalid_gofs_template_id == given_task_template_id

    def test_with_invalid_field_ids(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_ids = ["field_0", "field_1", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFieldIds(given_field_ids)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_field_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_field_ids.call_args
        error_object = call_args[0][0]
        invalid_field_ids = error_object.field_ids
        assert invalid_field_ids == given_field_ids

    def test_with_duplicate_field_ids_to_a_gof(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_duplicate_field_ids = ["field_0", "field_0"]
        given_field_ids = given_duplicate_field_ids + ["field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = DuplicateFieldIdsToGoF(given_gof_id,
                                                  given_duplicate_field_ids)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_duplicate_field_ids_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_field_ids_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_duplicate_field_ids_to_a_gof.call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_duplicate_field_ids

    def test_with_invalid_field_ids_to_a_gof(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_gof_id = "gof_0"
        given_field_ids = ["field_0", "field_0", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFieldsOfGoF(given_gof_id, given_field_ids)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_fields_given_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_fields_given_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_invalid_fields_given_to_a_gof \
            .call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_field_ids

    def test_with_user_who_does_not_have_write_permission_to_a_gof(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_created_by_id = "user_0"
        given_gof_id = "gof_0"
        given_required_user_roles = ["role_1", "role_2"]
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(size=1,
                                                                    gof_id=given_gof_id)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs,
                created_by_id=given_created_by_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsGoFWritablePermission

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserNeedsGoFWritablePermission(
            given_created_by_id, given_gof_id, given_required_user_roles)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_user_needs_gof_writable_permission.return_value \
            = \
            mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_gof_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_gof_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_gof_id = error_object.gof_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_gof_id == given_gof_id
        assert required_roles == given_required_user_roles

    def test_with_user_who_does_not_have_write_permission_to_a_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_created_by_id = "user_0"
        given_required_user_roles = ["role_1", "role_2"]
        given_field_id = "field_0"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs,
                created_by_id=given_created_by_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = UserNeedsFieldWritablePermission(
            given_created_by_id, given_field_id, given_required_user_roles)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_user_needs_field_writable_permission \
            .return_value \
            = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_field_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_field_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_field_id = error_object.field_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_field_id == given_field_id
        assert required_roles == given_required_user_roles

    def test_with_empty_response_to_a_required_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = ""
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = EmptyValueForRequiredField(given_field_id)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_empty_value_in_required_field \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_empty_value_in_required_field \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_empty_value_in_required_field \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        assert invalid_field_id == given_field_id

    def test_with_invalid_response_to_a_phone_number_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "890808"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidPhoneNumberValue(given_field_id,
                                                   given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_phone_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_phone_number_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_email_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "sljlsjls@gmail"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidEmailFieldValue(given_field_id,
                                                  given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_email_address \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_email_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_email_address \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_url_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidURLValue(given_field_id,
                                           given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_url_address \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_url_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_url_address.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_weak_password_response_to_a_password_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "weak password"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = NotAStrongPassword(given_field_id,
                                              given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_weak_password \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_weak_password \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_weak_password.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_number_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidNumberValue(given_field_id,
                                              given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_number_value \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_number_value.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_float_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "two point five"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFloatValue(given_field_id,
                                             given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_float_value \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_float_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_float_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_dropdown_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidValueForDropdownField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_dropdown_value \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_dropdown_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_dropdown_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_dropdown_choices = error_object.valid_values

        assert invalid_field_id == given_field_id
        assert valid_dropdown_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_name_to_a_gof_selector_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["gof selector name 1", "gof selector name 2"]
        given_field_response = '["gof selector name 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectNameInGoFSelectorField(
            given_field_id, given_field_response, valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_name_in_gof_selector \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_gof_selector_choices = error_object.valid_gof_selector_names

        assert invalid_field_id == given_field_id
        assert valid_gof_selector_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_radio_group_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectRadioGroupChoice(
            given_field_id, given_field_response, valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_choice_in_radio_group_field \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_radio_group_choices = error_object.valid_radio_group_options

        assert invalid_field_id == given_field_id
        assert valid_radio_group_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_check_box_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_checkbox_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_checkbox_options_selected)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectCheckBoxOptionsSelected(
            given_field_id, invalid_checkbox_options_selected, valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_checkbox_group_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_check_box_response = error_object.invalid_checkbox_options
        valid_check_box_choices = error_object.valid_check_box_options

        assert invalid_field_id == given_field_id
        assert invalid_check_box_response == invalid_checkbox_options_selected
        assert valid_check_box_choices == valid_choices

    def test_with_invalid_option_to_a_multi_select_options_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_options_selected)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectMultiSelectOptionsSelected(
            given_field_id, invalid_multi_select_options_selected,
            valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_options_response = \
            error_object.invalid_multi_select_options
        valid_multi_select_options = error_object.valid_multi_select_options

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_options_response == \
               invalid_multi_select_options_selected
        assert valid_multi_select_options == valid_choices

    def test_with_invalid_option_to_a_multi_select_label_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_labels_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_labels_selected)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = IncorrectMultiSelectLabelsSelected(
            given_field_id, invalid_multi_select_labels_selected, valid_choices
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_labels_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_labels_response = \
            error_object.invalid_multi_select_labels
        valid_multi_select_labels = error_object.valid_multi_select_labels

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_labels_response == \
               invalid_multi_select_labels_selected
        assert valid_multi_select_labels == valid_choices

    def test_with_invalid_date_format_to_a_date_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        from ib_tasks.constants.config import DATE_FORMAT
        expected_format = DATE_FORMAT
        given_field_response = "05-04-2020"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidDateFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_date_format \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_date_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_date_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_time_format_to_a_time_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        given_field_response = "2:30 PM"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidTimeFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_time_format \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_time_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_time_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_url_to_a_image_uploader_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid image url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidUrlForImage(given_field_id,
                                              given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.raise_invalid_image_url.return_value = \
            mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_image_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_image_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_image_url = error_object.image_url

        assert invalid_field_id == given_field_id
        assert given_field_response == invalid_image_url

    def test_with_invalid_image_format_to_a_image_uploader_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid image format url"
        given_format = ".svg"
        allowed_formats = [".png", ".jpeg"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidImageFormat(given_field_id, given_format,
                                              allowed_formats)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_image_format \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_image_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_image_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_invalid_url_to_a_file_uploader_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid file url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidUrlForFile(given_field_id,
                                             given_field_response)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_invalid_file_url \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_file_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_file_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_file_url = error_object.file_url

        assert invalid_field_id == given_field_id
        assert invalid_file_url == given_field_response

    def test_with_invalid_file_format_to_a_file_uploader_field(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_field_id = "field_0"
        given_field_response = "invalid file format url"
        given_format = ".zip"
        allowed_formats = [".pdf", ".xls"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        transition_checklist_gofs = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                transition_checklist_gofs=transition_checklist_gofs)
        task_storage_mock.check_is_valid_task_display_id.return_value = True

        task_id = 1
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = True
        create_or_update_task_storage_mock.get_template_id_for_given_task \
            .return_value \
            = "template_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat

        perform_base_validations_for_template_gofs_and_fields_mock \
            .side_effect = InvalidFileFormat(given_field_id, given_format,
                                             allowed_formats)
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_file_format \
            .return_value = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_file_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_file_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_valid_details(
            self, create_or_update_task_storage_mock, template_storage_mock,
            stage_action_storage_mock, task_storage_mock, gof_storage_mock,
            storage_mock, field_storage_mock, mock_object, presenter_mock,
            perform_base_validations_for_template_gofs_and_fields_mock
    ):
        # Arrange
        given_task_display_id = "task_1"
        task_id = 1
        transition_checklist_dto = \
            CreateTransitionChecklistTemplateWithTaskDisplayIdDTOFactory(
                task_display_id=given_task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = \
            task_id
        create_or_update_task_storage_mock.is_valid_task_id.return_value = \
            True
        gof_ids = [
            gof_dto.gof_id for gof_dto in
            transition_checklist_dto.transition_checklist_gofs
        ]
        same_gof_orders = [
            gof_dto.same_gof_order for gof_dto in
            transition_checklist_dto.transition_checklist_gofs
        ]
        expected_task_gofs = TaskGoFWithTaskIdDTOFactory.build_batch(
            size=len(gof_ids), task_id=task_id,
            gof_id=factory.Iterator(gof_ids),
            same_gof_order=factory.Iterator(same_gof_orders)
        )
        expected_task_gof_details = TaskGoFDetailsDTOFactory.build_batch(
            size=len(gof_ids), gof_id=factory.Iterator(gof_ids),
            same_gof_order=factory.Iterator(same_gof_orders)
        )
        create_or_update_task_storage_mock.create_task_gofs.return_value = \
            expected_task_gof_details
        expected_task_gof_ids = [0, 0, 1, 1]
        expected_task_gof_fields = TaskGoFFieldDTOFactory.build_batch(
            size=len(expected_task_gof_ids),
            task_gof_id=factory.Iterator(expected_task_gof_ids)
        )
        interactor = CreateOrUpdateTransitionChecklistTemplateInteractor(
            create_or_update_task_storage=create_or_update_task_storage_mock,
            template_storage=template_storage_mock,
            stage_action_storage=stage_action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            storage=storage_mock, field_storage=field_storage_mock
        )
        presenter_mock.get_create_transition_checklist_response.return_value \
            = mock_object

        # Act
        response = interactor.create_transition_checklist_wrapper(
            transition_checklist_dto, presenter_mock)

        # Assert
        assert response == mock_object
        create_or_update_task_storage_mock.create_task_gofs \
            .assert_called_once_with(task_gof_dtos=expected_task_gofs)
        create_or_update_task_storage_mock.create_task_gof_fields \
            .assert_called_once_with(expected_task_gof_fields)
