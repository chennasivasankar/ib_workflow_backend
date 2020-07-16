from typing import List
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.models import User, Team, TeamMember
from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, BasicTeamDTO, TeamMembersDTO
)


class TeamStorageImplementation(TeamStorageInterface):

    def is_user_admin(self, user_id: str):
        try:
            User.objects.get(user_id=user_id, is_admin=True)
        except User.DoesNotExist:
            raise UserHasNoAccess()

    def get_team_dtos(
            self, user_id: str, pagination_dto: PaginationDTO
    ) -> (List[BasicTeamDTO], int):
        team_objects = Team.objects.all()
        total_teams = len(team_objects)
        offset = pagination_dto.offset
        limit = pagination_dto.limit
        team_objects = team_objects[offset:offset + limit]
        team_dtos_list = self._get_team_dtos_list(team_objects=team_objects)
        return (team_dtos_list, total_teams)

    @staticmethod
    def _get_team_dtos_list(team_objects):
        team_dtos = [
            BasicTeamDTO(
                team_id=str(team_object.team_id),
                name=team_object.name,
                description=team_object.description
            )
            for team_object in team_objects
        ]
        return team_dtos

    def get_team_member_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamMembersDTO]:
        team_members = TeamMember.objects.filter(
            team__team_id__in=team_ids
        ).values_list('team__team_id', 'member_id')
        from collections import defaultdict
        team_member_ids_dict = defaultdict(list)
        for team_member in team_members:
            team_id = str(team_member[0])
            team_member_ids_dict[team_id].extend([team_member[1]])
        team_member_ids_dtos = [
            TeamMembersDTO(
                team_id=team_id,
                member_ids=team_member_ids_dict[team_id]
            ) for team_id in team_ids
        ]
        return team_member_ids_dtos
