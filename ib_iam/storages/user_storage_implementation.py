from typing import List

from ib_iam.interactors.storage_interfaces.dtos import UserDTO, UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, RoleIdAndNameDTO, TeamIdAndNameDTO, \
    CompanyIdAndNameDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class UserStorageImplementation(UserStorageInterface):
    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def is_user_exist(self, user_id: str) -> bool:
        from ib_iam.models import UserDetails
        is_exists = UserDetails.objects.filter(user_id=user_id).exists()
        return is_exists

    def get_role_objs_ids(self, roles):
        from ib_iam.models import Role
        role_ids = Role.objects.filter(role_id__in=roles) \
            .values_list('id', flat=True)
        return role_ids

    def check_are_valid_role_ids(self, role_ids):
        from ib_iam.models import Role
        role_objs_count = Role.objects.filter(
            role_id__in=role_ids).count()
        are_exists = role_objs_count == len(role_ids)
        return are_exists

    def check_is_exists_company_id(self, company_id):
        from ib_iam.models import Company
        is_exist = Company.objects.filter(company_id=company_id).exists()
        return is_exist

    def check_are_valid_team_ids(self, team_ids):
        from ib_iam.models import Team
        team_objs_count = Team.objects.filter(
            team_id__in=team_ids).count()
        are_exists = team_objs_count == len(team_ids)
        return are_exists

    def remove_roles_for_user(self, user_id: str):
        from ib_iam.models import UserRole
        UserRole.objects.filter(user_id=user_id).delete()

    def remove_teams_for_user(self, user_id: str):
        from ib_iam.models import UserTeam
        UserTeam.objects.filter(user_id=user_id).delete()

    def add_roles_to_the_user(self, user_id: str, role_ids: List[str]):
        from ib_iam.models import UserRole
        user_roles = [UserRole(user_id=user_id, role_id=str(role_id))
                      for role_id in role_ids]
        UserRole.objects.bulk_create(user_roles)

    def add_user_to_the_teams(self, user_id: str, team_ids: List[str]):
        from ib_iam.models import UserTeam
        user_teams = [UserTeam(user_id=user_id, team_id=team_id)
                      for team_id in team_ids]
        UserTeam.objects.bulk_create(user_teams)

    def change_company_for_user(self, company_id: str, user_id: str):
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        user.company_id = company_id
        user.save()

    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str]):
        self.create_user(company_id, is_admin, user_id)
        self.add_user_to_the_teams(user_id, team_ids)
        self.add_roles_to_the_user(user_id, role_ids)

    @staticmethod
    def create_user(company_id, is_admin, user_id):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=is_admin,
                                   company_id=company_id)

    def get_users_who_are_not_admins(self, offset, limit) -> List[UserDTO]:
        from ib_iam.models import UserDetails
        user_dtos = []
        users = UserDetails.objects. \
                    filter(is_admin=False)[offset: offset + limit]
        for user in users:
            user_dtos.append(UserDTO(
                user_id=user.user_id,
                is_admin=user.is_admin,
                company_id=str(user.company_id)
            ))
        return user_dtos

    def get_total_count_of_users_for_query(self):
        from ib_iam.models import UserDetails
        total_count_of_users = \
            UserDetails.objects.filter(is_admin=False).count()
        return total_count_of_users

    def get_team_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserTeamDTO]:
        from ib_iam.models import UserTeam
        user_teams = UserTeam.objects.filter(user_id__in=user_ids) \
            .select_related('team')
        team_dtos = []
        for user_team in user_teams:
            team = user_team.team
            team_dto = UserTeamDTO(
                user_id=user_team.user_id,
                team_id=str(team.team_id),
                team_name=team.name
            )
            team_dtos.append(team_dto)
        return team_dtos

    def get_role_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserRoleDTO]:
        from ib_iam.models import UserRole
        user_roles = UserRole.objects.filter(user_id__in=user_ids) \
            .select_related('role')
        role_dtos = []
        for user_role in user_roles:
            role = user_role.role
            role_dto = UserRoleDTO(
                user_id=user_role.user_id,
                role_id=str(role.role_id),
                name=role.name,
                description=role.description
            )
            role_dtos.append(role_dto)
        return role_dtos

    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        from ib_iam.models import UserDetails
        user_companies = UserDetails.objects.filter(user_id__in=user_ids) \
            .select_related('company')
        company_dtos = []
        for user_company in user_companies:
            company = user_company.company
            company_dto = UserCompanyDTO(
                user_id=user_company.user_id,
                company_id=str(company.company_id),
                company_name=company.name
            )
            company_dtos.append(company_dto)
        return company_dtos

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
