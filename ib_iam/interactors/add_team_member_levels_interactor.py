import collections
from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface \
    import TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class DuplicateLevelHierarchies(Exception):
    def __init__(self, level_hierarchies: List[int]):
        self.level_hierarchies = level_hierarchies


class NegativeLevelHierarchy(Exception):
    def __init__(self, level_hierarchies: List[int]):
        self.level_hierarchies = level_hierarchies


class DuplicateTeamMemberLevelNames(Exception):
    def __init__(self, team_member_level_names: List[str]):
        self.team_member_level_names = team_member_level_names


class AddTeamMemberLevelsInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface
    ):
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def add_team_member_levels_wrapper(
            self, team_id: str, user_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO],
            presenter: AddTeamMemberLevelsPresenterInterface
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin

        try:
            response = self._add_team_member_levels_response(
                team_id=team_id, user_id=user_id,
                team_member_level_dtos=team_member_level_dtos,
                presenter=presenter
            )
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin()
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        except DuplicateLevelHierarchies as err:
            response = presenter.response_for_duplicate_level_hierarchies(err)
        except NegativeLevelHierarchy as err:
            response = presenter.response_for_negative_level_hierarchies(err)
        except DuplicateTeamMemberLevelNames as err:
            response = presenter.response_for_duplicate_team_member_level_names(
                err)
        return response

    def _add_team_member_levels_response(
            self, team_id: str, user_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO],
            presenter: AddTeamMemberLevelsPresenterInterface
    ):
        self.add_team_member_levels(
            team_id=team_id, user_id=user_id,
            team_member_level_dtos=team_member_level_dtos)
        response = presenter. \
            prepare_success_response_for_add_team_member_levels_to_team()
        return response

    def add_team_member_levels(
            self, team_id: str, user_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]
    ):
        level_hierarchies = [
            team_member_level_dto.level_hierarchy
            for team_member_level_dto in team_member_level_dtos
        ]
        team_member_level_names = [
            team_member_level_dto.team_member_level_name
            for team_member_level_dto in team_member_level_dtos
        ]
        self._validate_duplicate_level_hierarchies(
            level_hierarchies=level_hierarchies)
        self._validate_negative_level_hierarchies(
            level_hierarchies=level_hierarchies)
        self._validate_duplicate_team_member_level_names(
            team_member_level_names=team_member_level_names
        )
        self._validate_is_user_admin(user_id=user_id)
        self.team_member_level_storage.validate_team_id(team_id=team_id)

        self.team_member_level_storage.add_team_member_levels(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos
        )
        return

    @staticmethod
    def _validate_negative_level_hierarchies(level_hierarchies: List[int]):
        negative_level_hierarchies = [
            level_hierarchy
            for level_hierarchy in level_hierarchies if level_hierarchy < 0
        ]
        if negative_level_hierarchies:
            raise NegativeLevelHierarchy(
                level_hierarchies=negative_level_hierarchies)

    @staticmethod
    def _validate_duplicate_level_hierarchies(level_hierarchies: List[int]):
        duplicate_level_hierarchies = [
            level_hierarchy
            for level_hierarchy, count in
            collections.Counter(level_hierarchies).items() if count > 1
        ]
        if duplicate_level_hierarchies:
            raise DuplicateLevelHierarchies(
                level_hierarchies=duplicate_level_hierarchies)
        return

    @staticmethod
    def _validate_duplicate_team_member_level_names(
            team_member_level_names: List[str]):
        duplicate_team_member_level_names = [
            team_member_level_name
            for team_member_level_name, count in
            collections.Counter(team_member_level_names).items() if count > 1
        ]
        if duplicate_team_member_level_names:
            raise DuplicateTeamMemberLevelNames(
                team_member_level_names=duplicate_team_member_level_names)
        return
