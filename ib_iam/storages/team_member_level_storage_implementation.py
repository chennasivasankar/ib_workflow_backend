from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import UsersNotBelongToGivenLevelHierarchy, \
    InvalidTeamId, InvalidLevelHierarchyOfTeam, UserNotBelongToTeam
from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO, MemberIdWithSubordinateMemberIdsDTO
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface


class TeamMemberLevelStorageImplementation(TeamMemberLevelStorageInterface):

    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]):
        from ib_iam.models.team_member_level import TeamMemberLevel
        TeamMemberLevel.objects.filter(
            team_id=team_id).delete()
        team_member_level_objects = [
            TeamMemberLevel(
                team_id=team_id,
                level_name=level_dto.team_member_level_name,
                level_hierarchy=level_dto.level_hierarchy
            )
            for level_dto in team_member_level_dtos
        ]
        TeamMemberLevel.objects.bulk_create(team_member_level_objects)
        return

    def get_team_member_level_details_dtos(self, team_id: str) -> \
            List[TeamMemberLevelDetailsDTO]:
        from ib_iam.models.team_member_level import TeamMemberLevel
        team_member_level_objects = TeamMemberLevel.objects.filter(
            team_id=team_id)
        team_member_level_details_dtos = [
            TeamMemberLevelDetailsDTO(
                team_member_level_id=str(team_member_level_object.id),
                team_member_level_name=team_member_level_object.level_name,
                level_hierarchy=team_member_level_object.level_hierarchy
            )
            for team_member_level_object in team_member_level_objects
        ]
        return team_member_level_details_dtos

    def add_members_to_levels_for_a_team(
            self, team_member_level_id_with_member_ids_dtos: List[
                TeamMemberLevelIdWithMemberIdsDTO]
    ):
        for team_member_level_id_with_member_ids_dto in team_member_level_id_with_member_ids_dtos:
            self._add_members_to_team_member_level(
                team_member_level_id_with_member_ids_dto=team_member_level_id_with_member_ids_dto
            )

    @staticmethod
    def _add_members_to_team_member_level(
            team_member_level_id_with_member_ids_dto: TeamMemberLevelIdWithMemberIdsDTO):
        from ib_iam.models import TeamMemberLevel
        team_member_level_id = \
            team_member_level_id_with_member_ids_dto.team_member_level_id
        team_member_level_object = \
            TeamMemberLevel.objects.get(id=team_member_level_id)
        team_id = team_member_level_object.team_id

        member_ids = team_member_level_id_with_member_ids_dto.member_ids
        from ib_iam.models import TeamUser
        TeamUser.objects.filter(
            team_member_level=team_member_level_object
        ).update(team_member_level=None)
        TeamUser.objects.filter(
            team_id=team_id, user_id__in=member_ids
        ).update(team_member_level=team_member_level_object)

    def get_member_details(self, team_id: str, level_hierarchy: int) \
            -> List[MemberDTO]:
        from ib_iam.models import TeamUser
        member_id_with_immediate_superior_user_id_list = \
            TeamUser.objects.filter(
                team_id=team_id,
                team_member_level__level_hierarchy=level_hierarchy
            ).values("user_id", "immediate_superior_team_user__user_id")

        member_dtos = [
            MemberDTO(
                member_id=member_id_with_immediate_superior_user_id_dict[
                    "user_id"],
                immediate_superior_team_user_id=
                member_id_with_immediate_superior_user_id_dict[
                    "immediate_superior_team_user__user_id"]
            )
            for member_id_with_immediate_superior_user_id_dict in
            member_id_with_immediate_superior_user_id_list
        ]
        return member_dtos

    def add_members_to_superiors(
            self, team_id: str, member_level_hierarchy: int,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        from ib_iam.models import TeamUser
        for immediate_superior_user_id_with_member_ids_dto in immediate_superior_user_id_with_member_ids_dtos:
            TeamUser.objects.filter(
                team_id=team_id,
                team_member_level__level_hierarchy=member_level_hierarchy,
                immediate_superior_team_user__user_id=immediate_superior_user_id_with_member_ids_dto.immediate_superior_user_id
            ).update(immediate_superior_team_user=None)

        for immediate_superior_user_id_with_member_ids_dto in immediate_superior_user_id_with_member_ids_dtos:
            self._add_members_to_superior(
                immediate_superior_user_id_with_member_ids_dto=immediate_superior_user_id_with_member_ids_dto,
                member_level_hierarchy=member_level_hierarchy,
                team_id=team_id)
        return

    def get_immediate_superior_user_id(self, team_id: str, user_id: str) -> \
            Optional[str]:
        from ib_iam.models import TeamUser
        user_team_object = TeamUser.objects.get(
            team_id=team_id, user_id=user_id
        )
        immediate_superior_team_user_object = \
            user_team_object.immediate_superior_team_user
        if immediate_superior_team_user_object:
            return immediate_superior_team_user_object.user_id
        return

    @staticmethod
    def _add_members_to_superior(
            immediate_superior_user_id_with_member_ids_dto: ImmediateSuperiorUserIdWithUserIdsDTO,
            member_level_hierarchy: int, team_id: str
    ):
        member_ids = \
            immediate_superior_user_id_with_member_ids_dto.member_ids
        immediate_superior_user_id = \
            immediate_superior_user_id_with_member_ids_dto.immediate_superior_user_id
        from ib_iam.models import TeamUser
        user_team_object = TeamUser.objects.get(
            user_id=immediate_superior_user_id, team_id=team_id)
        TeamUser.objects.filter(
            team_id=team_id,
            team_member_level__level_hierarchy=member_level_hierarchy,
            user_id__in=member_ids
        ).update(
            immediate_superior_team_user=user_team_object
        )

    def get_member_id_with_subordinate_member_ids_dtos(
            self, team_id: str, member_ids: List[str]
    ) -> List[MemberIdWithSubordinateMemberIdsDTO]:
        member_ids = list(set(member_ids))
        from ib_iam.models import TeamUser
        user_team_objects = TeamUser.objects.filter(
            team_id=team_id, user_id__in=member_ids
        )
        member_id_with_subordinate_member_ids_dtos = [
            self.get_member_id_with_subordinate_member_ids_dto(
                user_team_object)
            for user_team_object in user_team_objects
        ]
        return member_id_with_subordinate_member_ids_dtos

    @staticmethod
    def get_member_id_with_subordinate_member_ids_dto(user_team_object):
        subordinate_member_ids = \
            user_team_object.subordinate_members.values_list(
                "user_id", flat=True
            )
        subordinate_member_ids = [
            str(subordinate_member_id)
            for subordinate_member_id in subordinate_member_ids
        ]
        member_id_with_subordinate_member_ids_dto = \
            MemberIdWithSubordinateMemberIdsDTO(
                member_id=str(user_team_object.user_id),
                subordinate_member_ids=subordinate_member_ids
            )
        return member_id_with_subordinate_member_ids_dto

    def validate_team_id(self, team_id: str) -> Optional[InvalidTeamId]:
        from ib_iam.models import Team
        team_objects = Team.objects.filter(team_id=team_id)
        is_team_objects_not_exists = not team_objects.exists()
        if is_team_objects_not_exists:
            raise InvalidTeamId
        return

    def get_team_member_level_ids(self, team_id: str) -> List[str]:
        from ib_iam.models import TeamMemberLevel
        team_member_level_ids = TeamMemberLevel.objects.filter(
            team_id=team_id
        ).values_list(
            "id", flat=True
        )
        team_member_level_ids = list(map(str, list(team_member_level_ids)))
        return team_member_level_ids

    def get_team_member_ids(self, team_id: str) -> List[str]:
        from ib_iam.models import TeamUser
        user_ids = TeamUser.objects.filter(
            team_id=team_id
        ).values_list(
            "user_id", flat=True
        )
        user_ids = list(map(str, list(user_ids)))
        return user_ids

    def validate_level_hierarchy_of_team(
            self, team_id: str, level_hierarchy: int
    ) -> Optional[InvalidLevelHierarchyOfTeam]:
        from ib_iam.models import TeamMemberLevel
        team_member_level_objects = TeamMemberLevel.objects.filter(
            team_id=team_id, level_hierarchy=level_hierarchy
        )
        is_team_member_level_objects_not_exists = \
            not team_member_level_objects.exists()
        if is_team_member_level_objects_not_exists:
            raise InvalidLevelHierarchyOfTeam
        return

    def validate_users_belong_to_given_level_hierarchy_in_a_team(
            self, team_id: str, user_ids: List[str], level_hierarchy: int
    ) -> [UsersNotBelongToGivenLevelHierarchy, InvalidLevelHierarchyOfTeam]:
        from ib_iam.models import TeamMemberLevel, TeamUser
        try:
            team_member_level_object = TeamMemberLevel.objects.get(
                team_id=team_id, level_hierarchy=level_hierarchy
            )
        except TeamMemberLevel.DoesNotExist:
            raise InvalidLevelHierarchyOfTeam
        user_ids_in_database = TeamUser.objects.filter(
            team_id=team_id, team_member_level=team_member_level_object
        ).values_list(
            "user_id", flat=True
        )

        user_ids_not_found = [
            user_id
            for user_id in user_ids if user_id not in user_ids_in_database
        ]
        if user_ids_not_found:
            raise UsersNotBelongToGivenLevelHierarchy(
                user_ids=user_ids_not_found,
                level_hierarchy=level_hierarchy
            )
        return

    def validate_user_in_a_team(self, team_id: str, user_id: str) \
            -> Optional[UserNotBelongToTeam]:
        from ib_iam.models import TeamUser
        team_user_objects = TeamUser.objects.filter(
            team_id=team_id, user_id=user_id)

        is_team_user_objects_not_exists = not team_user_objects.exists()
        if is_team_user_objects_not_exists:
            raise UserNotBelongToTeam
        return
