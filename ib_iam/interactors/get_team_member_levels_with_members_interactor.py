from ib_iam.interactors.dtos.dtos import CompleteTeamMemberLevelsDetailsDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsWithMembersPresenterInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface


class GetTeamMemberLevelsWithMembersInteractor:

    def __init__(self,
                 team_member_level_storage: TeamMemberLevelStorageInterface):
        self.team_member_level_storage = team_member_level_storage

    def get_team_member_levels_with_members_wrapper(
            self, team_id: str,
            presenter: GetTeamMemberLevelsWithMembersPresenterInterface
    ):
        # TODO: Validate the team id
        response = self._get_team_member_levels_with_members_response(
            team_id=team_id, presenter=presenter
        )
        return response

    def _get_team_member_levels_with_members_response(
            self, team_id: str,
            presenter: GetTeamMemberLevelsWithMembersPresenterInterface
    ):
        complete_team_member_levels_details_dto = \
            self.get_team_member_levels_with_members(team_id=team_id)
        response = presenter.prepare_success_response_for_team_member_levels_with_members(
            complete_team_member_levels_details_dto=complete_team_member_levels_details_dto
        )
        return response

    def get_team_member_levels_with_members(self, team_id) -> \
            CompleteTeamMemberLevelsDetailsDTO:
        # TODO: Optimisation should be done
        from ib_iam.interactors.get_team_member_levels_interactor import \
            GetTeamMemberLevelsInteractor
        from ib_iam.interactors.get_team_members_of_level_hierarchy_interactor \
            import GetTeamMembersOfLevelHierarchyInteractor
        from ib_iam.interactors.dtos.dtos import \
            TeamMemberLevelIdWithMemberIdsDTO

        get_team_member_levels_interactor = GetTeamMemberLevelsInteractor(
            team_member_level_storage=self.team_member_level_storage
        )
        team_member_level_details_dtos = \
            get_team_member_levels_interactor.get_team_member_levels(
                team_id=team_id
            )
        get_team_members_of_level_hierarchy_interactor = \
            GetTeamMembersOfLevelHierarchyInteractor(
                team_member_level_storage=self.team_member_level_storage
            )

        team_member_dtos = []
        team_user_profile_dtos = []
        team_member_level_id_with_member_ids_dtos = []
        for team_member_level_details_dto in team_member_level_details_dtos:
            member_dtos, user_profile_dtos = \
                get_team_members_of_level_hierarchy_interactor.get_team_members_of_level_hierarchy(
                    team_id=team_id,
                    level_hierarchy=team_member_level_details_dto.level_hierarchy
                )
            team_member_dtos.append(member_dtos)
            team_user_profile_dtos.append(user_profile_dtos)
            team_member_ids = [member_dto.member_id for member_dto in
                               member_dtos]
            team_member_level_id_with_member_ids_dtos.append(
                TeamMemberLevelIdWithMemberIdsDTO(
                    team_member_level_id=team_member_level_details_dto.team_member_level_id,
                    member_ids=team_member_ids
                )
            )

        member_ids = [
            member_dto.member_id
            for member_dto in team_member_dtos
        ]

        member_id_with_subordinate_member_ids_dtos = \
            self.team_member_level_storage.get_member_id_with_subordinate_member_ids_dtos(
                team_id=team_id, member_ids=member_ids
            )

        complete_team_member_levels_details_dto = \
            CompleteTeamMemberLevelsDetailsDTO(
                member_dtos=team_member_dtos,
                user_profile_dtos=team_user_profile_dtos,
                team_member_level_details_dtos=team_member_level_details_dtos,
                team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
                member_id_with_subordinate_member_ids_dtos=member_id_with_subordinate_member_ids_dtos
            )
        return complete_team_member_levels_details_dto
