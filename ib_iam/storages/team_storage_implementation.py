from typing import List, Optional, Tuple

from ib_iam.exceptions.custom_exceptions import InvalidTeamId
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamNameAndDescriptionDTO, TeamIdAndNameDTO, PaginationDTO, TeamUserIdsDTO,
    TeamsWithTotalTeamsCountDTO, TeamWithTeamIdAndUserIdsDTO, TeamDTO,
    TeamWithUserIdDTO, UserWithTeamDTO)
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.models import Team, TeamUser


class TeamStorageImplementation(TeamStorageInterface):

    def get_teams_with_total_teams_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> TeamsWithTotalTeamsCountDTO:

        from django.db.models.functions import Lower
        team_objects = Team.objects.all().order_by(Lower('name'))
        total_teams_count = len(team_objects)
        offset = pagination_dto.offset
        limit = pagination_dto.limit
        team_objects = team_objects[offset:offset + limit]
        team_dtos_list = self._convert_to_team_dtos(team_objects=team_objects)
        teams_with_total_teams_count_dto = TeamsWithTotalTeamsCountDTO(
            teams=team_dtos_list,
            total_teams_count=total_teams_count
        )
        return teams_with_total_teams_count_dto

    def get_team_user_ids_dtos(
            self, team_ids: List[str]
    ) -> List[TeamUserIdsDTO]:
        team_users = TeamUser.objects.filter(
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
            TeamUser(
                team_id=team_id,
                user_id=user_id
            ) for user_id in user_ids
        ]
        TeamUser.objects.bulk_create(team_members)

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

    def get_member_ids_of_team(self, team_id: str) -> List[str]:
        member_ids = TeamUser.objects.filter(
            team_id=team_id
        ).values_list("user_id", flat=True)
        return list(member_ids)

    def delete_members_from_team(self, team_id: str, user_ids: List[str]):
        TeamUser.objects.filter(team_id=team_id, user_id__in=user_ids) \
            .delete()

    def delete_team(self, team_id: str):
        Team.objects.filter(team_id=team_id).delete()

    def get_valid_team_ids(self, team_ids: List[str]) -> List[str]:
        team_ids = Team.objects.filter(team_id__in=team_ids) \
            .values_list("team_id", flat=True)
        team_ids = list(map(str, team_ids))
        return team_ids

    def get_team_dtos(self, team_ids: List[str]) -> List[TeamDTO]:
        team_objects = Team.objects.filter(team_id__in=team_ids)
        team_dtos = self._convert_to_team_dtos(team_objects)
        return team_dtos

    @staticmethod
    def _convert_to_team_dtos(team_objects):
        team_dtos = [
            TeamDTO(
                team_id=str(team_object.team_id), name=team_object.name,
                description=team_object.description
            ) for team_object in team_objects
        ]
        return team_dtos

    def get_team_id_and_name_dtos(
            self, team_ids: List[str]) -> List[TeamIdAndNameDTO]:
        team_objects = Team.objects.filter(team_id__in=team_ids)
        return [TeamIdAndNameDTO(
            team_id=team_object.team_id, team_name=team_object.name
        ) for team_object in team_objects]

    def get_team_user_dtos(
            self, user_ids: List[str], team_ids: List[str]
    ) -> List[TeamWithUserIdDTO]:
        user_team_objects = TeamUser.objects.filter(
            team_id__in=team_ids, user_id__in=user_ids
        ).select_related('team')
        user_team_dtos = [
            TeamWithUserIdDTO(
                user_id=str(user_team_object.user_id),
                team_id=str(user_team_object.team.team_id),
                team_name=user_team_object.team.name
            ) for user_team_object in user_team_objects
        ]
        return user_team_dtos

    def is_team_exist(self, team_id: str) -> bool:
        # todo write tests for this
        return Team.objects.filter(team_id=team_id).exists

    def get_or_create_team_with_name(self, name: str) -> Tuple[str, bool]:
        team_object, is_created = Team.objects.get_or_create(
            name=name
        )
        return str(team_object.team_id), is_created

    def get_or_create_team_with_id_and_name(self, team_id, name: str) -> bool:
        _, is_created = Team.objects.get_or_create(
            team_id=team_id, name=name
        )
        return is_created

    def get_user_with_team_dtos(self, user_ids: List[str]) -> List[UserWithTeamDTO]:
        team_user_objects = TeamUser.objects.filter(user_id__in=user_ids)
        user_with_team_dtos = [
            UserWithTeamDTO(
                user_id=team_user_object.user_id,
                team_id=team_user_object.team_id
            )
            for team_user_object in team_user_objects
        ]
        return user_with_team_dtos

    def add_user_to_team(
            self, user_id: str, team_id: str, team_member_level_id: str
    ):
        TeamUser.objects.create(
            user_id=user_id, team_id=team_id,
            team_member_level_id=team_member_level_id
        )
        return
