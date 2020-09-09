from ib_iam.exceptions.custom_exceptions import InvalidLevelHierarchyOfTeam
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMembersOfLevelHierarchyPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface


class GetTeamMembersOfLevelHierarchyInteractor:

    def __init__(self,
                 team_member_level_storage: TeamMemberLevelStorageInterface):
        self.team_member_level_storage = team_member_level_storage

    def get_team_members_of_level_hierarchy_wrapper(
            self, team_id: str, level_hierarchy: int,
            presenter: GetTeamMembersOfLevelHierarchyPresenterInterface):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        try:
            response = self._get_team_members_of_level_hierarchy_response(
                team_id=team_id, level_hierarchy=level_hierarchy,
                presenter=presenter
            )
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        except InvalidLevelHierarchyOfTeam:
            response = presenter.response_for_invalid_level_hierarchy_of_team()
        return response

    def _get_team_members_of_level_hierarchy_response(
            self, team_id: str, level_hierarchy: int,
            presenter: GetTeamMembersOfLevelHierarchyPresenterInterface):
        member_dtos, user_profile_dtos = \
            self.get_team_members_of_level_hierarchy(
                team_id=team_id, level_hierarchy=level_hierarchy
            )
        response = presenter.prepare_success_response_for_get_team_members_of_level_hierarchy(
            member_dtos=member_dtos, user_profile_dtos=user_profile_dtos
        )
        return response

    def get_team_members_of_level_hierarchy(
            self, team_id: str, level_hierarchy: int):
        self.team_member_level_storage.validate_team_id(team_id=team_id)
        self.team_member_level_storage.validate_level_hierarchy_of_team(
            team_id=team_id, level_hierarchy=level_hierarchy
        )

        member_dtos = self.team_member_level_storage.get_member_details(
            team_id=team_id, level_hierarchy=level_hierarchy
        )
        user_ids = [member_dto.member_id for member_dto in member_dtos]

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        user_profile_dtos = service_adapter.user_service.get_user_profile_bulk(
            user_ids=user_ids
        )
        return member_dtos, user_profile_dtos

    def get_immediate_superior_user_id(self, team_id: str, user_id: str):
        # TODO: validate team id and user id
        immediate_superior_user_id = \
            self.team_member_level_storage.get_immediate_superior_user_id(
                team_id=team_id, user_id=user_id
            )
        return immediate_superior_user_id
