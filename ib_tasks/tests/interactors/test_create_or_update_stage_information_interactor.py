from unittest.mock import create_autospec, patch

import pytest

from ib_boards.exceptions.custom_exceptions import InvalidTemplateFields
from ib_tasks.exceptions.roles_custom_exceptions import \
    InvalidStageRolesException
from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageValues, \
    DuplicateStageIds, InvalidStageDisplayLogic, \
    InvalidStagesDisplayName
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidStagesTaskTemplateId, InvalidTaskTemplateIds
from ib_tasks.interactors.create_or_update_stages import \
    CreateOrUpdateStagesInteractor
from ib_tasks.interactors.get_stage_display_logic_interactor import StageDisplayLogicInteractor
from ib_tasks.interactors.stages_dtos import StageLogicAttributes
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TemplateFieldsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import \
    TaskTemplateStorageInterface
from ib_tasks.interactors.task_dtos import StatusOperandStageDTO
from ib_tasks.tests.common_fixtures.adapters.roles_service import get_valid_role_ids_in_given_role_ids
from ib_tasks.tests.factories.storage_dtos import StageDTOFactory, \
    TaskStagesDTOFactory, ValidStageDTOFactory


class TestCreateOrUpdateStageInformation:

    @pytest.fixture
    def create_stage_dtos(self):
        StageDTOFactory.reset_sequence()
        return StageDTOFactory.create_batch(
            size=2, value=-1
        )

    @pytest.fixture
    def create_task_stages_dtos(self):
        TaskStagesDTOFactory.reset_sequence()
        return TaskStagesDTOFactory.create_batch(size=2)

    @pytest.fixture()
    def valid_stages_dto(self):
        return ValidStageDTOFactory.create_batch(size=1,
                                                 stage_id="stage_id_1")

    @pytest.fixture()
    def stage_storage(self):
        return create_autospec(StageStorageInterface)

    @pytest.fixture()
    def task_storage(self):
        return create_autospec(TaskStorageInterface)

    @pytest.fixture()
    def task_template_storage(self):
        return create_autospec(TaskTemplateStorageInterface)

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_given_invalid_roles_raises_exception(
            self, logic_interactor, mocker,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage):
        # Arrange
        StageDTOFactory.reset_sequence()
        create_stage_dtos = StageDTOFactory.create_batch(
            size=2, value=-1, roles="ROLE"
        )

        stage_ids = ["stage_id_1", "stage_id_2"]
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=stage_storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        stage_storage.validate_stages_related_task_template_ids. \
            return_value = []
        stage_storage.get_existing_status_ids.return_value = ["status1"]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]

        stage_storage.get_existing_stage_ids.side_effect = [[], ["stage_id_1"]]

        # Act
        with pytest.raises(InvalidStageRolesException) as error:
            stage_interactor.create_or_update_stages(
                stages_details=create_stage_dtos
            )

        # Assert
        mocker_obj.assert_called_once()

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_create_stage_given_valid_information_creates_stage_with_given_information(
            self, logic_interactor, mocker, create_stage_dtos,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage):
        # Arrange

        stage_ids = ["stage_id_1", "stage_id_2"]
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=stage_storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]
        stage_storage.validate_stages_related_task_template_ids. \
            return_value = []

        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]

        stage_storage.get_existing_status_ids.return_value = ["status1"]
        stage_storage.get_existing_stage_ids.side_effect = [[], []]

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=create_stage_dtos
        )

        # Assert
        stage_storage.get_existing_stage_ids.assert_called()
        stage_storage.create_stages.assert_called_once_with(
            create_stage_dtos
        )

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_create_and_update_stage_given_valid_information_creates_and_updates(
            self, logic_interactor, create_stage_dtos,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage, mocker):
        # Arrange

        stage_ids = ["stage_id_1", "stage_id_2"]
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=stage_storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )
        stage_storage.validate_stages_related_task_template_ids. \
            return_value = []

        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]
        get_valid_role_ids_in_given_role_ids(mocker)
        stage_storage.get_existing_status_ids.return_value = ["status1"]
        stage_storage.get_existing_stage_ids.side_effect = [[], ["stage_id_1"]]

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=create_stage_dtos
        )

        # Assert
        stage_storage.get_existing_stage_ids.assert_called()
        stage_storage.create_stages.assert_called_once_with(
            create_stage_dtos
        )

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_update_stage_when_stage_id_already_exists_for_given_task_template_updates_stage_details(
            self, logic_interactor, mocker, create_stage_dtos,
            create_task_stages_dtos,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage):
        # Arrange
        stages_details = create_stage_dtos

        storage = stage_storage
        storage.get_existing_stage_ids.return_value = \
            ["stage_id_1", "stage_id_2"]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]
        storage.validate_stages_related_task_template_ids.return_value = []
        task_stages_dto = create_task_stages_dtos
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        stage_storage.get_existing_status_ids.return_value = ["status1"]
        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]

        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act

        stage_interactor.create_or_update_stages(
            stages_details=stages_details
        )
        # Assert
        storage.validate_stages_related_task_template_ids. \
            assert_called_once_with(task_stages_dto)
        storage.update_stages.assert_called_once_with(
            stages_details
        )

    def test_validate_values_when_given_invalid_values_raises_exception(
            self, mocker, stage_storage, task_storage, task_template_storage):
        # Arrange
        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            value=-2, size=2
        )
        storage = stage_storage
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        storage.get_existing_stage_ids.return_value = []
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(InvalidStageValues) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_invalid_task_template_id_with_valid_stage_id_raises_exception(
            self, logic_interactor, mocker, create_stage_dtos,
            create_task_stages_dtos,
            task_template_storage
    ):
        # Arrange
        stages_details = create_stage_dtos
        task_stages_dto = create_task_stages_dtos
        storage = create_autospec(StageStorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        storage.get_existing_status_ids.return_value = ["status1"]
        storage.get_existing_stage_ids.return_value = [
            "stage_id_1", "stage_id_2"
        ]
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]
        storage.validate_stages_related_task_template_ids. \
            return_value = ["PR_PENDING RP APPROVAL"]
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]

        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = task_template_ids

        # Act
        with pytest.raises(InvalidStagesTaskTemplateId) as err:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids \
            .assert_called_once_with(task_template_ids)
        storage.validate_stages_related_task_template_ids. \
            assert_called_once_with(task_stages_dto)

    def test_check_for_duplicate_stage_ids_raises_exception(self,
                                                            task_template_storage):
        # Arrange
        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_id="stage_id_1", size=2
        )
        storage = create_autospec(StageStorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        storage.get_existing_stage_ids.return_value = []
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["FIN_PR"]
        storage.validate_stages_related_task_template_ids.return_value = []

        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(DuplicateStageIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    def test_validate_task_template_ids_if_doesnot_exists_raises_exception(
            self, mocker, create_stage_dtos, task_template_storage):
        # Arrange
        stages_details = create_stage_dtos
        storage = create_autospec(StageStorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids \
            .return_value = [
            ""]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]

        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            assert_called_once_with(task_template_ids)

    def test_validate_stage_display_name_invalid_stage_display_name_raises_exception(
            self, stage_storage, task_storage, task_template_storage):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_display_name="", size=2
        )
        storage = stage_storage
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(InvalidStagesDisplayName) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_validate_fields_of_given_task_template_raises_exception(
            self, logic_interactor, mocker, create_stage_dtos,
            create_task_stages_dtos, valid_stages_dto, task_storage,
            stage_storage, task_template_storage):
        # Arrange
        stages_details = create_stage_dtos

        storage = stage_storage
        storage.get_existing_stage_ids.return_value = \
            ["stage_id_0", "stage_id_1"]
        storage.validate_stages_related_task_template_ids.return_value = []
        stage_storage.get_existing_status_ids.return_value = ["status1"]
        task_stages_dto = create_task_stages_dtos
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status1",
            operator="==",
            stage="stage_id_1"
        )]
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import get_valid_role_ids_in_given_role_ids
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        mocker_obj.return_value = ["role_id_1", "role_id_2", "role_id_0"]

        valid_template_ids = ["task_template_id_1", "task_template_id_2"]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = valid_template_ids

        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_0"]
            )]
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(InvalidTemplateFields):
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_storage.get_field_ids_for_given_task_template_ids.assert_called_once_with(
            valid_template_ids
        )

    @patch.object(StageDisplayLogicInteractor,
                  'get_stage_display_logic_condition')
    def test_validate_stage_display_logic_invalid_stage_display_logic_raises_exception(
            self, logic_interactor, task_template_storage, mocker):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_display_logic="status1 == stage_id_1", size=2
        )
        storage = create_autospec(StageStorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        logic_interactor.return_value = [StatusOperandStageDTO(
            variable="status10",
            operator="==",
            stage="stage_id_1"
        )]
        storage.get_existing_stage_ids.return_value = []
        storage.get_existing_status_ids.return_value = []
        get_valid_role_ids_in_given_role_ids(mocker)
        task_storage.get_field_ids_for_given_task_template_ids.return_value = [TemplateFieldsDTO(
            task_template_id="task_template_id_1",
            field_ids=["field_id_1", "field_id_2"]
        ),
            TemplateFieldsDTO(
                task_template_id="task_template_id_2",
                field_ids=["field_id_1", "field_id_2"]
            )]
        task_template_storage.get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]

        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )

        # Act
        with pytest.raises(InvalidStageDisplayLogic) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
