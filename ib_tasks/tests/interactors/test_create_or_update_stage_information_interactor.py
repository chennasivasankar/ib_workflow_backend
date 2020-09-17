import pytest

from ib_boards.exceptions.custom_exceptions import InvalidTemplateFields
from ib_tasks.exceptions.roles_custom_exceptions import \
    InvalidStageRolesException
from ib_tasks.exceptions.stage_custom_exceptions import (
    InvalidStageValues, DuplicateStageIds, InvalidStageDisplayLogic,
    InvalidStagesDisplayName)
from ib_tasks.exceptions.task_custom_exceptions import \
    (InvalidStagesTaskTemplateId, InvalidTaskTemplateIds)
from ib_tasks.interactors.create_or_update_stages import \
    CreateOrUpdateStagesInteractor
from ib_tasks.interactors.task_dtos import (StatusOperandStageDTO,
                                            StageDisplayLogicDTO)
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_valid_role_ids_in_given_role_ids
from ib_tasks.tests.common_fixtures.interactors import \
    get_stage_display_logic_mock
from ib_tasks.tests.factories.interactor_dtos import TemplateFieldsDTOFactory
from ib_tasks.tests.factories.storage_dtos import (StageDTOFactory,
                                                   TaskStagesDTOFactory,
                                                   ValidStageDTOFactory)
from ib_tasks.tests.interactors.storage_method_mocks import StorageMethodsMock


class TestCreateOrUpdateStageInformation(StorageMethodsMock):

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageDTOFactory.reset_sequence()
        TemplateFieldsDTOFactory.reset_sequence(1)

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

    @staticmethod
    @pytest.fixture
    def stage_interactor(stage_storage, task_storage, task_template_storage):
        stage_interactor = CreateOrUpdateStagesInteractor(
            stage_storage=stage_storage, task_storage=task_storage,
            task_template_storage=task_template_storage
        )
        return stage_interactor

    @staticmethod
    def interactors_mock(mocker):
        stage_logics = [StageDisplayLogicDTO(
            current_stage="stage_id_1",
            display_logic_dto=StatusOperandStageDTO(
                variable="status1",
                operator="==",
                stage="stage_id_1"))]
        get_stage_display_logic_mock(mocker, stage_logics)

    @staticmethod
    def adapters_mock(mocker):
        mocker_obj = get_valid_role_ids_in_given_role_ids(mocker)
        return mocker_obj

    @staticmethod
    @pytest.fixture
    def storage_method_mocks(task_storage, task_template_storage):
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1", "task_template_id_2"]
        task_storage.get_field_ids_for_given_task_template_ids.return_value \
            = TemplateFieldsDTOFactory.create_batch(2, field_ids=[
            "field_id_1", "field_id_2"])

    def test_given_invalid_roles_raises_exception(
            self, mocker, stage_interactor, storage_method_mocks,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage):
        # Arrange
        valid_status_ids = ["status1"]
        roles = ["ROLE"]
        StageDTOFactory.reset_sequence()
        create_stage_dtos = StageDTOFactory.create_batch(
            size=2, value=-1, roles="ROLE"
        )

        mocker_obj = self.adapters_mock(mocker)

        stage_storage.validate_stages_related_task_template_ids. \
            return_value = []
        stage_storage.get_existing_status_ids.return_value = valid_status_ids

        # Act
        with pytest.raises(InvalidStageRolesException) as error:
            stage_interactor.create_or_update_stages(
                stages_details=create_stage_dtos
            )

        # Assert
        mocker_obj.assert_called_once_with(roles)

    def test_create_stage_given_valid_information_creates_stage_with_given_information(
            self, mocker, create_stage_dtos, stage_interactor,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage, storage_method_mocks):
        # Arrange
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)
        valid_status_ids = ["status1"]
        valid_template_stages = []
        stage_storage.validate_stages_related_task_template_ids. \
            return_value = valid_template_stages

        stage_storage.get_existing_status_ids.return_value = valid_status_ids

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=create_stage_dtos
        )

        # Assert
        stage_storage.get_existing_stage_ids.assert_called()
        stage_storage.create_stages.assert_called_once_with(
            create_stage_dtos
        )

    def test_create_and_update_stage_given_valid_information_creates_and_updates(
            self, create_stage_dtos, stage_interactor, storage_method_mocks,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage, mocker):
        # Arrange

        valid_template_stages = []
        stage_storage.validate_stages_related_task_template_ids. \
            return_value = valid_template_stages
        valid_status_ids = ["status1"]
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)
        stage_storage.get_existing_status_ids.return_value = valid_status_ids

        # Act
        stage_interactor.create_or_update_stages(
            stages_details=create_stage_dtos
        )

        # Assert
        stage_storage.get_existing_stage_ids.assert_called()
        stage_storage.create_stages.assert_called_once_with(
            create_stage_dtos
        )

    def test_update_stage_when_stage_id_already_exists_for_given_task_template_updates_stage_details(
            self, mocker, create_stage_dtos, stage_interactor,
            create_task_stages_dtos, storage_method_mocks,
            valid_stages_dto, task_storage, stage_storage,
            task_template_storage):
        # Arrange
        stages_details = create_stage_dtos
        valid_status_ids = ["status1"]
        storage = stage_storage
        storage.get_existing_stage_ids.return_value = \
            ["stage_id_1", "stage_id_2"]
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)
        valid_template_stages = []
        storage.validate_stages_related_task_template_ids.return_value = \
            valid_template_stages
        task_stages_dto = create_task_stages_dtos
        stage_storage.get_existing_status_ids.return_value = valid_status_ids

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
            self, mocker, stage_storage, task_storage, task_template_storage,
            stage_interactor, storage_method_mocks):
        # Arrange
        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            value=-2, size=2
        )
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)

        # Act
        with pytest.raises(InvalidStageValues) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    def test_invalid_task_template_id_with_valid_stage_id_raises_exception(
            self, mocker, create_stage_dtos, stage_interactor,
            create_task_stages_dtos, task_storage, stage_storage,
            task_template_storage, storage_method_mocks
    ):
        # Arrange
        stage_ids = ["stage_id_1", "stage_id_2"]
        status_ids = ["status1"]
        valid_template_stages = ["PR_PENDING RP APPROVAL"]
        stages_details = create_stage_dtos
        task_stages_dto = create_task_stages_dtos
        stage_storage.get_existing_status_ids.return_value = status_ids
        stage_storage.get_existing_stage_ids.return_value = stage_ids

        stage_storage.validate_stages_related_task_template_ids. \
            return_value = valid_template_stages
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)

        # Act
        with pytest.raises(InvalidStagesTaskTemplateId) as err:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .assert_called_once_with(task_template_ids)
        stage_storage.validate_stages_related_task_template_ids. \
            assert_called_once_with(task_stages_dto)

    def test_check_for_duplicate_stage_ids_raises_exception(
            self, task_storage, stage_storage, storage_method_mocks,
            stage_interactor, task_template_storage):
        # Arrange
        stage_ids = []
        valid_template_stages = []
        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_id="stage_id_1", size=2
        )
        stage_storage.get_existing_stage_ids.return_value = stage_ids
        stage_storage.validate_stages_related_task_template_ids.return_value \
            = valid_template_stages

        # Act
        with pytest.raises(DuplicateStageIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    def test_validate_task_template_ids_if_doesnot_exists_raises_exception(
            self, mocker, create_stage_dtos, task_template_storage,
            stage_storage, task_storage, stage_interactor):
        # Arrange
        stages_details = create_stage_dtos
        task_template_ids = ["task_template_id_1", "task_template_id_2"]
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = ["task_template_id_1"]

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids. \
            assert_called_once_with(task_template_ids)

    def test_validate_stage_display_name_invalid_stage_display_name_raises_exception(
            self, stage_storage, task_storage, task_template_storage,
            stage_interactor):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_display_name="", size=2
        )

        # Act
        with pytest.raises(InvalidStagesDisplayName) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    def test_validate_fields_of_given_task_template_raises_exception(
            self, mocker, create_stage_dtos, stage_interactor,
            template_fields_dto,
            create_task_stages_dtos, valid_stages_dto, task_storage,
            stage_storage, task_template_storage, storage_method_mocks):
        # Arrange
        stages_details = create_stage_dtos
        valid_template_ids = ["task_template_id_1", "task_template_id_2"]
        storage = stage_storage
        storage.get_existing_stage_ids.return_value = \
            ["stage_id_0", "stage_id_1"]
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids. \
            return_value = valid_template_ids
        task_storage.get_field_ids_for_given_task_template_ids.return_value \
            = template_fields_dto
        storage.validate_stages_related_task_template_ids.return_value = []
        stage_storage.get_existing_status_ids.return_value = ["status1"]
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)

        # Act
        with pytest.raises(InvalidTemplateFields):
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert
        task_storage.get_field_ids_for_given_task_template_ids \
            .assert_called_once_with(
            valid_template_ids
        )

    def test_validate_stage_display_logic_invalid_stage_display_logic_raises_exception(
            self, task_template_storage, stage_storage, task_storage, mocker,
            stage_interactor, storage_method_mocks):
        # Arrange

        StageDTOFactory.reset_sequence()
        stages_details = StageDTOFactory.create_batch(
            stage_display_logic="status1 == stage_id_1", size=2
        )
        storage = stage_storage

        storage.get_existing_stage_ids.return_value = []
        self.interactors_mock(mocker)
        self.adapters_mock(mocker)

        # Act
        with pytest.raises(InvalidStageDisplayLogic) as error:
            stage_interactor.create_or_update_stages(
                stages_details=stages_details
            )

        # Assert

    @pytest.fixture
    def template_fields_dto(self):
        return TemplateFieldsDTOFactory.create_batch(2)
