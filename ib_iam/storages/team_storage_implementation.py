from typing import List
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.models import UserDetails, Team, TeamMember
from ib_iam.exceptions.custom_exceptions import UserHasNoAccess, TeamNameAlreadyExists
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamDTO, TeamMemberIdsDTO, TeamNameAndDescriptionDTO,
    TeamsWithTotalTeamsCountDTO
)


class TeamStorageImplementation(TeamStorageInterface):

    def raise_exception_if_user_is_not_admin(self, user_id: str):
        try:
            UserDetails.objects.get(user_id=user_id, is_admin=True)
        except UserDetails.DoesNotExist:
            raise UserHasNoAccess

    def get_teams_with_total_teams_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> TeamsWithTotalTeamsCountDTO:
        team_objects = Team.objects.all()
        total_teams_count = len(team_objects)
        offset = pagination_dto.offset
        limit = pagination_dto.limit
        team_objects = team_objects[offset:offset + limit]
        team_dtos_list = self._get_team_dtos(team_objects=team_objects)
        teams_with_total_teams_count_dto = TeamsWithTotalTeamsCountDTO(
            teams=team_dtos_list,
            total_teams_count=total_teams_count
        )
        return teams_with_total_teams_count_dto

    def get_team_member_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamMemberIdsDTO]:
        team_members = TeamMember.objects.filter(
            team__team_id__in=team_ids
        ).values_list('team__team_id', 'member_id')
        from collections import defaultdict
        team_member_ids_dictionary = defaultdict(list)
        for team_member in team_members:
            team_id = str(team_member[0])
            team_member_ids_dictionary[team_id].extend([team_member[1]])
        team_member_ids_dtos = [
            TeamMemberIdsDTO(
                team_id=team_id,
                member_ids=team_member_ids_dictionary[team_id]
            ) for team_id in team_ids
        ]
        return team_member_ids_dtos

    def is_team_name_already_exists(self, name: str):
        is_team_name_already_exists = \
            Team.objects.filter(name=name).exists()
        return is_team_name_already_exists

    def add_team(
            self,
            user_id: str,
            team_name_and_description_dto: TeamNameAndDescriptionDTO
    ) -> str:
        team_object = Team.objects.create(
            name=team_name_and_description_dto.name,
            description=team_name_and_description_dto.description,
            created_by=user_id
        )
        return str(team_object.team_id)

    @staticmethod
    def _get_team_dtos(team_objects):
        team_dtos = [
            TeamDTO(
                team_id=str(team_object.team_id),
                name=team_object.name,
                description=team_object.description
            )
            for team_object in team_objects
        ]
        return team_dtos
