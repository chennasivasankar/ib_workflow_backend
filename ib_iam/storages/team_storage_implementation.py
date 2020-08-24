from typing import List, Optional

from ib_iam.exceptions.custom_exceptions import InvalidTeamId
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamNameAndDescriptionDTO, PaginationDTO, TeamUserIdsDTO, \
    TeamsWithTotalTeamsCountDTO, TeamWithTeamIdAndUserIdsDTO, TeamDTO, \
    TeamNameAndDescriptionDTO, TeamIdAndNameDTO
from ib_iam.app_interfaces.dtos import UserTeamsDTO

from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.models import Team, UserTeam
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamUserIdsDTO,
    TeamsWithTotalTeamsCountDTO, TeamWithUserIdsDTO,
    TeamWithTeamIdAndUserIdsDTO,
    TeamDTO)


class TeamStorageImplementation(TeamStorageInterface):

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

    def get_team_user_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamUserIdsDTO]:
        team_users = UserTeam.objects.filter(
            team__team_id__in=team_ids
        ).values_list('team__team_id', 'user_id')
        from collections import defaultdict
        team_user_ids_dictionary = defaultdict(list)
        for team_user in team_users:
            team_id = str(team_user[0])
            team_user_ids_dictionary[team_id].extend([team_user[1]])
        team_user_ids_dtos = [
            TeamUserIdsDTO(
                team_id=team_id,
                user_ids=team_user_ids_dictionary[team_id]
            ) for team_id in team_ids
        ]
        return team_user_ids_dtos

    def get_team_id_if_team_name_already_exists(
            self, name: str
    ) -> Optional[str]:
        try:
            team_object = Team.objects.get(name=name)
            return str(team_object.team_id)
        except Team.DoesNotExist:
            return None

    def add_team(self, user_id: str,
                 team_name_and_description_dto: TeamNameAndDescriptionDTO) -> \
            str:
        team_object = Team.objects.create(
            name=team_name_and_description_dto.name,
            description=team_name_and_description_dto.description,
            created_by=user_id)
        return str(team_object.team_id)

    def add_users_to_team(self, team_id: str, user_ids: List[str]):
        team_members = [
            UserTeam(
                team_id=team_id,
                user_id=user_id
            ) for user_id in user_ids
        ]
        UserTeam.objects.bulk_create(team_members)

    def raise_exception_if_team_not_exists(self, team_id: str):
        try:
            Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            raise InvalidTeamId()

    def update_team_details(
            self,
            team_dto: TeamWithTeamIdAndUserIdsDTO):
        Team.objects.filter(
            team_id=team_dto.team_id).update(
            name=team_dto.name,
            description=team_dto.description
        )

    def get_member_ids_of_team(self, team_id: str):
        member_ids = UserTeam.objects.filter(team_id=team_id) \
            .values_list("user_id", flat=True)
        return list(member_ids)

    def delete_all_members_of_team(self, team_id: str):
        UserTeam.objects.filter(team_id=team_id).delete()

    def delete_team(self, team_id: str):
        Team.objects.filter(team_id=team_id).delete()

    def get_valid_team_ids(self, team_ids: List[str]) -> List[str]:
        team_ids = Team.objects.filter(team_id__in=team_ids) \
            .values_list("team_id", flat=True)
        team_ids = list(map(str, team_ids))
        return team_ids

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

    def get_team_id_and_name_dtos(
            self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        team_objects = Team.objects.filter(team_id__in=team_ids)
        return [TeamIdAndNameDTO(
            team_id=team_object.team_id, team_name=team_object.name
        ) for team_object in team_objects]
