from typing import List

from ib_iam.exceptions.custom_exceptions import \
    UsersNotBelongToGivenLevelHierarchy, UserIsNotAdmin
from ib_iam.interactors.dtos.dtos import ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToSuperiorsPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface \
    import TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AddMembersToSuperiorsInteractor(ValidationMixin):

    def __init__(
            self, user_storage: UserStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface
    ):
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def add_members_to_superiors_wrapper(
            self, team_id: str, member_level_hierarchy: int,
            presenter: AddMembersToSuperiorsPresenterInterface,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO], user_id: str
    ):
        from ib_iam.exceptions.custom_exceptions import \
            InvalidTeamId, InvalidLevelHierarchyOfTeam, MemberIdsNotFoundInTeam
        try:
            response = self._add_members_to_superiors_response(
                team_id=team_id, member_level_hierarchy=member_level_hierarchy,
                presenter=presenter, user_id=user_id,
                immediate_superior_user_id_with_member_ids_dtos=
                immediate_superior_user_id_with_member_ids_dtos
            )
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin()
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        except InvalidLevelHierarchyOfTeam:
            response = presenter.response_for_invalid_level_hierarchy_of_team()
        except MemberIdsNotFoundInTeam as err:
            response = presenter.response_for_team_member_ids_not_found(err)
        except UsersNotBelongToGivenLevelHierarchy as err:
            response = presenter. \
                response_for_users_not_belong_to_team_member_level(err)
        return response

    def _add_members_to_superiors_response(
            self, team_id: str, member_level_hierarchy: int,
            presenter: AddMembersToSuperiorsPresenterInterface,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO], user_id: str
    ):
        self.add_members_to_superiors(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=
            immediate_superior_user_id_with_member_ids_dtos,
            user_id=user_id
        )
        response = \
            presenter.prepare_success_response_for_add_members_superiors()
        return response

    def add_members_to_superiors(
            self, team_id: str, member_level_hierarchy: int, user_id: str,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        self._validate_is_user_admin(user_id=user_id)
        self.team_member_level_storage.validate_team_id(team_id=team_id)
        self.team_member_level_storage.validate_level_hierarchy_of_team(
            team_id=team_id, level_hierarchy=member_level_hierarchy
        )
        self._validate_team_member_ids(
            immediate_superior_user_id_with_member_ids_dtos=
            immediate_superior_user_id_with_member_ids_dtos,
            team_id=team_id
        )
        self._validate_team_users_belong_to_given_level_hierarchy_in_a_team(
            immediate_superior_user_id_with_member_ids_dtos,
            member_level_hierarchy, team_id)
        self.team_member_level_storage.add_members_to_superiors(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=
            immediate_superior_user_id_with_member_ids_dtos
        )
        return

    def _validate_team_users_belong_to_given_level_hierarchy_in_a_team(
            self,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO],
            member_level_hierarchy: int, team_id: str
    ):
        subordinate_user_ids = []
        immediate_superior_user_ids = []
        for immediate_superior_user_id_with_member_ids_dto in \
                immediate_superior_user_id_with_member_ids_dtos:
            subordinate_user_ids.extend(
                immediate_superior_user_id_with_member_ids_dto.member_ids
            )
            immediate_superior_user_ids.append(
                immediate_superior_user_id_with_member_ids_dto.immediate_superior_user_id
            )
        self.team_member_level_storage. \
            validate_users_belong_to_given_level_hierarchy_in_a_team(
            user_ids=subordinate_user_ids, team_id=team_id,
            level_hierarchy=member_level_hierarchy
        )
        self.team_member_level_storage. \
            validate_users_belong_to_given_level_hierarchy_in_a_team(
            user_ids=immediate_superior_user_ids, team_id=team_id,
            level_hierarchy=member_level_hierarchy + 1
        )

    def _validate_team_member_ids(
            self, immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO],
            team_id: str
    ):
        team_member_ids_in_database = self.team_member_level_storage.get_team_member_ids(
            team_id=team_id
        )
        team_member_ids = self._get_team_member_ids_from_dto(
            immediate_superior_user_id_with_member_ids_dtos
        )
        member_ids_not_found_in_team = [
            team_member_id for team_member_id in team_member_ids
            if team_member_id not in team_member_ids_in_database
        ]
        from ib_iam.exceptions.custom_exceptions import \
            MemberIdsNotFoundInTeam
        if member_ids_not_found_in_team:
            raise MemberIdsNotFoundInTeam(
                team_member_ids=member_ids_not_found_in_team
            )

    @staticmethod
    def _get_team_member_ids_from_dto(
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ) -> List[str]:
        team_member_ids = []
        for immediate_superior_user_id_with_member_ids_dto in \
                immediate_superior_user_id_with_member_ids_dtos:
            team_member_ids.extend(
                immediate_superior_user_id_with_member_ids_dto.member_ids
            )
            team_member_ids.append(
                immediate_superior_user_id_with_member_ids_dto.immediate_superior_user_id
            )
        return team_member_ids
