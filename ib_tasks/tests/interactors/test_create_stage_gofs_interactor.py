import mock
import pytest

from ib_tasks.interactors.create_stage_gofs_interactor import \
    CreateStageGoFsInteractor
from ib_tasks.tests.factories.interactor_dtos import \
    StageIdWithGoFIdsDTOFactory, DBStageIdWithStageIdDTOFactory, \
    DBStageIdWithGoFIdDTOFactory, DBStageIdWithGoFIdsDTOFactory


class TestCreateStageGoFsInteractor:
    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface \
            import StageStorageInterface
        stage_storage = mock.create_autospec(StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import \
            GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageIdWithGoFIdsDTOFactory.reset_sequence(1)
        DBStageIdWithStageIdDTOFactory.reset_sequence(1)
        DBStageIdWithGoFIdDTOFactory.reset_sequence(1)
        DBStageIdWithGoFIdsDTOFactory.reset_sequence(1)

    def test_with_duplicate_stage_ids_raises_exception(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        stage_id = "stage_1"
        expected_duplicate_stage_ids = [stage_id]
        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(
                size=2, stage_id=stage_id)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds

        # Assert
        with pytest.raises(DuplicateStageIds) as err:
            interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
            )
        assert err.value.args[0] == expected_duplicate_stage_ids

    def test_with_duplicate_gof_ids_for_same_stage_raises_exception(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        gof_ids = ["gof_1", "gof_1"]
        expected_duplicate_gof_ids = ["gof_1"]
        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(
                size=2, gof_ids=gof_ids)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            DuplicateGoFIds

        # Assert
        with pytest.raises(DuplicateGoFIds) as err:
            interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
            )
        assert err.value.args[0] == expected_duplicate_gof_ids

    def test_with_invalid_stage_ids_raises_exception(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        expected_invalid_stage_id = ["stage_1", "stage_2"]
        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(size=2)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )

        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            return_value = []
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException

        # Assert
        with pytest.raises(InvalidStageIdsListException) as err:
            interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
            )
        assert err.value.args[0] == expected_invalid_stage_id
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            assert_called_once_with(stage_ids=expected_invalid_stage_id)

    def test_with_invalid_gof_ids_raises_exception(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        expected_stage_ids = ["stage_1", "stage_2"]
        expected_invalid_gof_ids = ["gof_1", "gof_2"]
        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(size=2)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            return_value = expected_stage_ids
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.return_value = []

        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds

        # Assert
        with pytest.raises(InvalidGoFIds) as err:
            interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
            )
        assert err.value.args[0] == expected_invalid_gof_ids
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.\
            assert_called_once_with(gof_ids=expected_invalid_gof_ids)

    def test_with_valid_data_creates_stage_gofs(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        expected_stage_ids = ["stage_1", "stage_2"]
        expected_db_stage_ids = [1, 2]
        expected_gof_ids = ["gof_1", "gof_2"]
        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(size=2)
        db_stage_id_with_stage_id_dtos = \
            DBStageIdWithStageIdDTOFactory.create_batch(size=2)
        db_stage_id_with_gof_ids_dtos = \
            DBStageIdWithGoFIdsDTOFactory.create_batch(size=2)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            return_value = expected_stage_ids
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.return_value = \
            expected_gof_ids
        stage_storage_mock.get_db_stage_ids_with_stage_ids_dtos.\
            return_value = db_stage_id_with_stage_id_dtos
        stage_storage_mock.get_existing_gof_ids_with_stage_id_of_stages.\
            return_value = []

        # Assert
        interactor.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
        )

        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        stage_storage_mock.get_db_stage_ids_with_stage_ids_dtos.\
            assert_called_once_with(stage_ids=expected_stage_ids)
        stage_storage_mock.get_existing_gof_ids_with_stage_id_of_stages.\
            assert_called_once_with(stage_ids=expected_db_stage_ids)
        stage_storage_mock.create_stage_gofs.assert_called_once_with(
            stage_id_with_gof_ids_dtos=db_stage_id_with_gof_ids_dtos)

    def test_with_some_existing_stage_gofs_does_not_creates_those_again(
            self, stage_storage_mock, gof_storage_mock):
        # Arrange
        expected_stage_ids = ["stage_1", "stage_2"]
        expected_db_stage_ids = [1, 2]
        expected_gof_ids = ["gof_1", "gof_2"]

        stage_id_with_gof_ids_dtos = \
            StageIdWithGoFIdsDTOFactory.create_batch(size=2)
        db_stage_id_with_stage_id_dtos = \
            DBStageIdWithStageIdDTOFactory.create_batch(size=2)
        db_stage_id_with_gof_id_dtos = \
            DBStageIdWithGoFIdDTOFactory.create_batch(size=1)
        db_stage_id_with_gof_ids_dtos = \
            DBStageIdWithGoFIdsDTOFactory.create_batch(size=2)

        interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage_mock,
            gof_storage=gof_storage_mock
        )
        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            return_value = expected_stage_ids
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.return_value = \
            expected_gof_ids
        stage_storage_mock.get_db_stage_ids_with_stage_ids_dtos.\
            return_value = db_stage_id_with_stage_id_dtos
        stage_storage_mock.get_existing_gof_ids_with_stage_id_of_stages.\
            return_value = db_stage_id_with_gof_id_dtos

        # Assert
        interactor.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos
        )

        stage_storage_mock.get_valid_stage_ids_in_given_stage_ids.\
            assert_called_once_with(stage_ids=expected_stage_ids)
        gof_storage_mock.get_valid_gof_ids_in_given_gof_ids.\
            assert_called_once_with(gof_ids=expected_gof_ids)
        stage_storage_mock.get_db_stage_ids_with_stage_ids_dtos.\
            assert_called_once_with(stage_ids=expected_stage_ids)
        stage_storage_mock.get_existing_gof_ids_with_stage_id_of_stages.\
            assert_called_once_with(stage_ids=expected_db_stage_ids)
        stage_storage_mock.create_stage_gofs.assert_called_once_with(
            stage_id_with_gof_ids_dtos=[db_stage_id_with_gof_ids_dtos[1]])
