from typing import List, Optional
from ib_iam.interactors.storage_interfaces.team_storage_interface import TeamStorageInterface
from ib_iam.models import UserDetails, Team, TeamMember
from ib_iam.exceptions.custom_exceptions import (
    UserHasNoAccess, TeamNameAlreadyExists, InvalidTeam
)
from ib_iam.interactors.storage_interfaces.dtos import (
    PaginationDTO, TeamDTO, TeamMemberIdsDTO,
    TeamsWithTotalTeamsCountDTO, TeamDetailsWithUserIdsDTO, TeamWithUserIdsDTO
)


class TeamStorageImplementation(TeamStorageInterface):

    def validate_is_user_admin(self, user_id: str):
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

    def get_valid_user_ids_among_the_given_user_ids(
            self, user_ids: List[str]
    ):
        user_ids = UserDetails.objects.filter(user_id__in=user_ids) \
            .values_list('user_id', flat=True)
        return list(user_ids)

    def add_team(
            self,
            user_id: str,
            team_details_with_user_ids_dto: TeamDetailsWithUserIdsDTO
    ) -> str:
        team_object = Team.objects.create(
            name=team_details_with_user_ids_dto.name,
            description=team_details_with_user_ids_dto.description,
            created_by=user_id
        )
        return str(team_object.team_id)

    def add_users_to_team(self, team_id: str, user_ids: List[str]):
        team_members = [
            TeamMember(
                team_id=team_id,
                member_id=user_id
            ) for user_id in user_ids
        ]
        TeamMember.objects.bulk_create(team_members)

    def raise_exception_if_team_not_exists(self, team_id: str):
        try:
            Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            raise InvalidTeam()

    def update_team_details(
            self, team_with_user_ids_dto: TeamWithUserIdsDTO
    ):
        Team.objects.filter(team_id=team_with_user_ids_dto.team_id).update(
            name=team_with_user_ids_dto.name,
            description=team_with_user_ids_dto.description
        )

    def get_member_ids_of_team(self, team_id: str):
        member_ids = TeamMember.objects.filter(team_id=team_id) \
                               .values_list("member_id", flat=True)
        return list(member_ids)

    def delete_members_from_team(self, team_id: str, member_ids: List[str]):
        TeamMember.objects.filter(team_id=team_id, member_id__in=member_ids) \
                  .delete()

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
