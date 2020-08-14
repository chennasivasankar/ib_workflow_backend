from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import TeamMemberLevelDetailsDTO
from ib_iam.interactors.storage_interfaces.level_storage_interface import \
    LevelStorageInterface


class LevelStorageImplementation(LevelStorageInterface):

    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]):
        from ib_iam.models.team_member_level import TeamMemberLevel
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

    def get_team_member_level_details_dtos(self, team_id: str) -> List[TeamMemberLevelDetailsDTO]:
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
        pass
