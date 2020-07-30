from typing import List

from ib_iam.interactors.storage_interfaces.dtos \
    import RoleIdAndNameDTO, CompanyIdAndNameDTO, TeamIdAndNameDTO
from ib_iam.interactors.storage_interfaces.get_user_options_storage_interface \
    import GetUserOptionsStorageInterface


class GetUserOptionsStorageImplementation(GetUserOptionsStorageInterface):
    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def get_companies(self) -> List[CompanyIdAndNameDTO]:
        from ib_iam.models import Company
        companies = []
        company_query_set = Company.objects.values('company_id', 'name')
        for company in company_query_set:
            companies.append(
                CompanyIdAndNameDTO(
                    company_id=str(company['company_id']),
                    company_name=company['name']
                )
            )
        return companies

    def get_teams(self) -> List[TeamIdAndNameDTO]:
        teams = []
        from ib_iam.models import Team
        team_query_set = Team.objects.values('team_id', 'name')
        for team in team_query_set:
            teams.append(
                TeamIdAndNameDTO(
                    team_id=str(team['team_id']),
                    team_name=team['name']
                )
            )
        return teams

    def get_roles(self) -> List[RoleIdAndNameDTO]:
        roles = []
        from ib_iam.models import Role
        role_query_set = Role.objects.values('role_id', 'name')
        for role in role_query_set:
            roles.append(
                RoleIdAndNameDTO(
                    role_id=str(role['role_id']),
                    name=role['name']
                )
            )
        return roles
