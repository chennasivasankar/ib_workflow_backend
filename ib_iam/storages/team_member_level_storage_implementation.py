from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamMemberLevelDetailsDTO, MemberDTO
from ib_iam.interactors.storage_interfaces.level_storage_interface import \
    TeamMemberLevelStorageInterface


class TeamMemberLevelStorageImplementation(TeamMemberLevelStorageInterface):

    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]):
        from ib_iam.models.team_member_level import TeamMemberLevel
        level_hierarchies = [
            team_member_level_dto.level_hierarchy
            for team_member_level_dto in team_member_level_dtos
        ]
        TeamMemberLevel.objects.filter(
            team_id=team_id, level_hierarchy__in=level_hierarchies).delete()
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
        from ib_iam.models import UserTeam
        UserTeam.objects.filter(
            team_id=team_id, user_id__in=member_ids
        ).update(team_member_level=team_member_level_object)

    def get_member_details(self, team_id: str, level_hierarchy: int) \
            -> List[MemberDTO]:
        from ib_iam.models import UserTeam
        member_id_with_immediate_superior_user_id_list = \
            UserTeam.objects.filter(
                team_id=team_id,
                team_member_level__level_hierarchy=level_hierarchy
            ).values("user_id", "immediate_superior_team_user_id")

        member_dtos = [
            MemberDTO(
                member_id=member_id_with_immediate_superior_user_id_dict[
                    "user_id"],
                immediate_superior_team_user_id=
                member_id_with_immediate_superior_user_id_dict[
                    "immediate_superior_team_user_id"]
            )
            for member_id_with_immediate_superior_user_id_dict in
            member_id_with_immediate_superior_user_id_list
        ]
        return member_dtos

    def add_members_to_superiors(
            self, team_id: str, level_hierarchy: int,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        for immediate_superior_user_id_with_member_ids_dto in immediate_superior_user_id_with_member_ids_dtos:
            self._add_members_to_superior(
                immediate_superior_user_id_with_member_ids_dto, level_hierarchy,
                team_id)

    @staticmethod
    def _add_members_to_superior(
            immediate_superior_user_id_with_member_ids_dto: ImmediateSuperiorUserIdWithUserIdsDTO,
            level_hierarchy: int, team_id: str
    ):
        member_ids = \
            immediate_superior_user_id_with_member_ids_dto.member_ids
        immediate_superior_user_id = \
            immediate_superior_user_id_with_member_ids_dto.immediate_superior_user_id
        from ib_iam.models import UserTeam
        UserTeam.objects.filter(
            team_id=team_id,
            team_member_level__level_hierarchy=level_hierarchy,
            user_id__in=member_ids
        ).update(
            immediate_superior_team_user_id=immediate_superior_user_id
        )
