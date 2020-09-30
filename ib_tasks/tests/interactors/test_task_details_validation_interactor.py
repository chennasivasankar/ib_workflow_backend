import datetime

import freezegun
import mock
import pytest

from ib_tasks.interactors.create_or_update_task. \
    task_details_validations_interactor import \
    TaskDetailsValidationsInteractor
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_valid_project_ids_mock
from ib_tasks.tests.factories.interactor_dtos import CreateTaskDTOFactory, \
    GoFFieldsDTOFactory, FieldValuesDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


class TestTaskDetailsValidationsInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.interactor_dtos import \
            BasicTaskDetailsDTOFactory
        CreateTaskDTOFactory.reset_sequence(1)
        BasicTaskDetailsDTOFactory.reset_sequence(1)
        FieldWithGoFDisplayNameDTOFactory.reset_sequence(1)
        GoFFieldsDTOFactory.reset_sequence(1)
        FieldValuesDTOFactory.reset_sequence(1)

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        return mock.create_autospec(TaskStorageInterface)

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def create_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        return mock.create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        return mock.create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def task_details_validation_storages_dto(
            self, task_storage_mock, task_template_storage_mock, storage_mock,
            action_storage_mock, gof_storage_mock, create_task_storage_mock,
            field_storage_mock
    ):
        from ib_tasks.interactors.create_or_update_task.\
            task_details_validations_interactor import \
            TaskDetailsValidationsStorages
        task_details_validation_storages = TaskDetailsValidationsStorages(
            task_template_storage=task_template_storage_mock,
            storage=storage_mock, action_storage=action_storage_mock,
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock
        )
        return task_details_validation_storages

    @pytest.fixture
    def gofs_details_validation_interactor_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".gofs_details_validations_interactor" \
               ".GoFsDetailsValidationsInteractor" \
               ".perform_gofs_details_validations"
        return mocker.patch(path)

    def test_with_invalid_action_id_raises_exception(
            self, task_details_validation_storages_dto):
        # Arrange
        invalid_action_id = 10
        stage_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__action_id=invalid_action_id)

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        task_details_validation_storages_dto.storage.validate_action.\
            return_value = False
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException

        # Assert
        with pytest.raises(InvalidActionException) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)
        assert err.value.args[0] == invalid_action_id

    def test_with_invalid_project_id_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        invalid_project_id = "project_100"
        valid_project_ids = ["project_1", "project_2"]
        stage_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__project_id=invalid_project_id)
        get_valid_project_ids_mock(mocker, valid_project_ids)

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.custom_exceptions import InvalidProjectId

        # Assert
        with pytest.raises(InvalidProjectId) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)
        assert err.value.args[0] == invalid_project_id

    def test_with_invalid_project_id_for_given_project_raises_exception(
            self, task_details_validation_storages_dto,
            gofs_details_validation_interactor_mock,
            mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["template_10"]
        task_dto = CreateTaskDTOFactory()
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        gofs_details_validation_interactor_mock(mocker)

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock_obj = \
            get_user_role_ids_based_on_project_mock(mocker)

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateOfProject
        get_user_role_ids_based_on_project_mock_obj.side_effect = \
            InvalidTaskTemplateOfProject(
                task_dto.basic_task_details_dto.project_id,
                task_dto.basic_task_details_dto.task_template_id)

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )

        # Assert
        with pytest.raises(InvalidTaskTemplateOfProject) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)

        assert err.value.args[0] == task_dto.basic_task_details_dto.project_id
        assert err.value.args[1] == \
               task_dto.basic_task_details_dto.task_template_id

    def test_with_due_datetime_without_start_datetime_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=None)
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeWithoutStartDateTimeIsNotValid

        # Assert
        with pytest.raises(DueDateTimeWithoutStartDateTimeIsNotValid) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)

        assert err.value.args[0] == \
               task_dto.basic_task_details_dto.due_datetime

    def test_without_priority_when_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__priority=None)
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.task_custom_exceptions import \
            PriorityIsRequired

        # Assert
        with pytest.raises(PriorityIsRequired):
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)

    def test_without_start_datetime_when_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=None,
            basic_task_details_dto__due_datetime=None,
        )
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateTimeIsRequired

        # Assert
        with pytest.raises(StartDateTimeIsRequired):
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)

    def test_without_due_datetime_when_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__due_datetime=None
        )
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeIsRequired

        # Assert
        with pytest.raises(DueDateTimeIsRequired):
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)

    def test_when_start_datetime_ahead_of_due_datetime_and_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]

        import datetime
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__due_datetime=datetime.datetime(2020, 9, 1),
            basic_task_details_dto__start_datetime=
            datetime.datetime(2020, 9, 9)
        )
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateIsAheadOfDueDate

        # Assert
        with pytest.raises(StartDateIsAheadOfDueDate) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)
        assert err.value.args[0] == \
               task_dto.basic_task_details_dto.start_datetime
        assert err.value.args[1] == \
               task_dto.basic_task_details_dto.due_datetime

    def test_when_due_datetime_expires_and_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]

        import datetime
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=
            datetime.datetime(2019, 9, 9),
            basic_task_details_dto__due_datetime=datetime.datetime(2020, 9, 1)
        )
        get_valid_project_ids_mock(mocker, valid_project_ids)
        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeHasExpired

        # Assert
        with pytest.raises(DueDateTimeHasExpired) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)
        assert err.value.args[0] == \
               task_dto.basic_task_details_dto.due_datetime

    @freezegun.freeze_time(datetime.datetime(2020, 8, 7))
    def test_when_user_does_not_fill_required_fields_and_action_type_is_not_no_validations_raises_exception(
            self, task_details_validation_storages_dto, mocker,
            gofs_details_validation_interactor_mock
    ):
        # Arrange
        stage_id = 1
        valid_project_ids = ["project_id_1"]
        task_template_ids_of_project = ["task_template_1"]

        field_values_dtos = FieldValuesDTOFactory.create_batch(
            size=2, field_response=None)
        gof_field_dtos = GoFFieldsDTOFactory.create_batch(
            size=2, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=
            datetime.datetime(2019, 9, 9),
            basic_task_details_dto__due_datetime=datetime.datetime(2020, 9, 1),
            gof_fields_dtos=gof_field_dtos
        )
        field_id_with_field_name_dtos = \
            FieldWithGoFDisplayNameDTOFactory.create_batch(size=2)

        get_valid_project_ids_mock(mocker, valid_project_ids)
        gofs_details_validation_interactor_mock(mocker)

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)

        task_details_validation_storages_dto.task_template_storage.\
            get_project_templates.return_value = task_template_ids_of_project
        task_details_validation_storages_dto.action_storage.\
            get_action_type_for_given_action_id.return_value = None

        task_details_validation_storages_dto.field_storage.\
            get_user_writable_fields_for_given_gof_ids.return_value = \
            field_id_with_field_name_dtos

        interactor = TaskDetailsValidationsInteractor(
            storages_dto=task_details_validation_storages_dto
        )
        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields

        # Assert
        with pytest.raises(UserDidNotFillRequiredFields) as err:
            interactor.perform_task_details_validations(
                task_dto=task_dto, stage_id=stage_id)
        assert err.value.args[0] == field_id_with_field_name_dtos
