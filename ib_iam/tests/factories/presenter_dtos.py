import factory, factory.django
from ib_iam.interactors.presenter_interfaces.dtos import TeamWithMembersDetailsDTO


class TeamWithMembersDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TeamWithMembersDetailsDTO

    total_teams_count = 0
    team_dtos = [
    ]
    team_member_ids_dtos = [
    ]
    member_dtos = [
    ]
