from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.team_interactor import TeamInteractor


class TestGetListOfTeamIdAndName:

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        mock = create_autospec(UserStorageInterface)
        return mock

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        mock = create_autospec(TeamStorageInterface)
        return mock

    def test_get_team_id_and_name_dtos_for_given_valid_details(
            self, user_storage_mock, team_storage_mock):
        team_ids = ["1"]
        from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO
        expected_result = [
            TeamIdAndNameDTO(team_id=team_ids[0], team_name="sample")
        ]
        interactor = TeamInteractor(
            user_storage=user_storage_mock, team_storage=team_storage_mock)
        team_storage_mock.get_team_id_and_name_dtos.return_value = \
            expected_result

        team_id_and_name_dtos = interactor.get_team_id_and_name_dtos(team_ids=team_ids)

        assert len(team_id_and_name_dtos) == len(expected_result)
        for index, team_id_and_name_dto in enumerate(team_id_and_name_dtos):
            assert expected_result[
                       index].team_name == team_id_and_name_dto.team_name
            assert expected_result[
                       index].team_id == team_id_and_name_dto.team_id

    def test_get_team_id_and_name_dtos_for_given_invalid_team_ids_then_raise_exception(
            self, user_storage_mock, team_storage_mock):
        team_ids = ["2"]
        interactor = TeamInteractor(
            user_storage=user_storage_mock, team_storage=team_storage_mock)
        from ib_iam.exceptions.custom_exceptions import InvalidTeamIds
        team_storage_mock.get_team_id_and_name_dtos.side_effect = \
            InvalidTeamIds

        with pytest.raises(InvalidTeamIds):
            interactor.get_team_id_and_name_dtos(team_ids=team_ids)
