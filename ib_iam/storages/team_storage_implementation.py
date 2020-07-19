from typing import List, Optional
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.models import UserDetails, Team, TeamMember
from ib_iam.exceptions.custom_exceptions import UserHasNoAccess, TeamNameAlreadyExists
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamDTO, TeamMemberIdsDTO,
    TeamsWithTotalTeamsCountDTO, AddTeamParametersDTO
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

    def get_team_id_if_team_name_already_exists(
            self, name: str
    ) -> Optional[str]:
        try:
            team_object = Team.objects.get(name=name)
            return str(team_object.team_id)
        except Team.DoesNotExist:
            return None

    def get_valid_member_ids_among_the_given_member_ids(
            self, member_ids: List[str]
    ):
        member_ids = UserDetails.objects.filter(user_id__in=member_ids) \
                                .values_list('user_id', flat=True)
        return list(member_ids)

    def add_team(
            self,
            user_id: str,
            add_team_parameters_dto: AddTeamParametersDTO
    ) -> str:
        team_object = Team.objects.create(
            name=add_team_parameters_dto.name,
            description=add_team_parameters_dto.description,
            created_by=user_id
        )
        return str(team_object.team_id)

    def add_members_to_team(self, team_id: str, member_ids: List[str]):
        team_members = [
            TeamMember(
                team_id=team_id,
                member_id=member_id
            ) for member_id in member_ids
        ]
        TeamMember.objects.bulk_create(team_members)

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
