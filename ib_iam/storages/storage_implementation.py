from typing import List

from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO, \
    UserRoleDTO, UserCompanyDTO, UserDTO, CompanyDTO, \
    TeamDTO, RoleIdAndNameDTO, RoleDTO
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_iam.models import Role


class StorageImplementation(StorageInterface):

    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models.user import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        return user.is_admin

    def get_users_who_are_not_admins(
            self, offset=0, limit=10) -> List[UserDTO]:
        from ib_iam.models import UserDetails
        user_dtos = []
        users = UserDetails.objects.filter(is_admin=False)[offset:limit]
        for user in users:
            user_dtos.append(UserDTO(
                user_id=user.user_id,
                is_admin=user.is_admin,
                company_id=str(user.company_id)
            ))
        return user_dtos

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
                role_id=str(role.id),
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

    def get_role_objs_ids(self, roles):
        role_ids = Role.objects.filter(role_id__in=roles) \
            .values_list('id', flat=True)
        return role_ids

    def add_new_user(self, user_id: str, is_admin: bool, company_id: str,
                     role_ids, team_ids: List[str]):
        self.create_user(company_id, is_admin, user_id)
        self.add_user_to_the_teams(team_ids, user_id)
        self.add_roles_to_the_user(role_ids, user_id)

    @staticmethod
    def add_roles_to_the_user(role_ids, user_id):
        from ib_iam.models import UserRole
        user_roles = [UserRole(user_id=user_id, role_id=str(role_id))
                      for role_id in role_ids]
        UserRole.objects.bulk_create(user_roles)

    @staticmethod
    def add_user_to_the_teams(team_ids, user_id):
        from ib_iam.models import UserTeam
        user_teams = [UserTeam(user_id=user_id, team_id=team_id)
                      for team_id in team_ids]
        UserTeam.objects.bulk_create(user_teams)

    @staticmethod
    def create_user(company_id, is_admin, user_id):
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=is_admin,
                                   company_id=company_id)

    def get_companies(self) -> List[CompanyDTO]:
        from ib_iam.models import Company
        companies = []
        company_query_set = Company.objects.values('company_id', 'name')
        for company in company_query_set:
            companies.append(
                CompanyDTO(
                    company_id=str(company['company_id']),
                    company_name=company['name']
                )
            )
        return companies

    def get_teams(self) -> List[TeamDTO]:
        teams = []
        from ib_iam.models import Team
        team_query_set = Team.objects.values('team_id', 'name')
        for team in team_query_set:
            teams.append(
                TeamDTO(
                    team_id=str(team['team_id']),
                    team_name=team['name']
                )
            )
        return teams

    def get_roles(self) -> List[RoleIdAndNameDTO]:
        roles = []
        from ib_iam.models import Role
        team_query_set = Role.objects.values('role_id', 'name')
        for role in team_query_set:
            roles.append(
                RoleIdAndNameDTO(
                    role_id=str(role['role_id']),
                    name=role['name']
                )
            )
        return roles

    def validate_role_ids(self, role_ids):
        from ib_iam.models import Role
        role_objs_count = Role.objects.filter(
            role_id__in=role_ids).count()
        are_exists = role_objs_count == len(role_ids)
        return are_exists

    def validate_company(self, company_id):
        from ib_iam.models import Company
        is_exist = Company.objects.filter(company_id=company_id).exists()
        return is_exist

    def validate_teams(self, team_ids):
        from ib_iam.models import Team
        team_objs_count = Team.objects.filter(
            team_id__in=team_ids).count()
        are_exists = team_objs_count == len(team_ids)
        return are_exists

    def create_roles(self, role_dtos: List[RoleDTO]):
        role_objects = [
            Role(role_id=role_dto.role_id, name=role_dto.name,
                 description=role_dto.description)
            for role_dto in role_dtos]
        Role.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        valid_role_ids = Role.objects.filter(role_id__in=role_ids).values_list(
            "role_id", flat=True
        )
        return list(valid_role_ids)

    def get_is_admin_of_given_user_id(self, user_id: int):
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)
        is_admin = user_object.is_admin
        return is_admin

    def validate_user_id(self, user_id):
        from ib_iam.models import UserDetails
        user_details_object = UserDetails.objects.filter(user_id=user_id)
        is_user_details_object_not_exist = not user_details_object.exists()
        if is_user_details_object_not_exist:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId
        return

    def validate_user_ids(self, user_ids: List[str]):
        from ib_iam.models import UserDetails
        valid_user_ids = UserDetails.objects.filter(
            user_id__in=user_ids
        ).values_list("user_id", flat=True)
        invalid_user_ids = [
            user_id
            for user_id in user_ids if user_id not in valid_user_ids
        ]
        if invalid_user_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidUserIds
            raise InvalidUserIds(user_ids=invalid_user_ids)
        return

    def get_user_role_ids(self, user_id: str):
        from ib_iam.models import UserRole
        role_ids = UserRole.objects.filter(
            user_id=user_id
        ).values_list("role__role_id", flat=True)
        return list(role_ids)

    def get_user_id_with_role_ids_dtos(self, user_ids: List[str]) \
            -> List[UserIdWithRoleIdsDTO]:
        from collections import defaultdict
        user_id_and_role_ids_dict = defaultdict(list)
        for user_id in user_ids:
            user_id_and_role_ids_dict[user_id] = []

        from ib_iam.models import UserRole
        user_id_and_role_ids = UserRole.objects.filter(
            user_id__in=user_ids
        ).values_list("user_id", "role__role_id")

        for user_id, role_id in user_id_and_role_ids:
            user_id_and_role_ids_dict[user_id].append(str(role_id))

        user_id_with_role_ids_dtos = self._prepare_user_id_with_role_ids_dtos(
            user_id_and_role_ids_dict=user_id_and_role_ids_dict
        )
        return user_id_with_role_ids_dtos

    def _prepare_user_id_with_role_ids_dtos(self, user_id_and_role_ids_dict):

        user_id_and_role_ids_dtos = [
            self._prepare_user_id_with_role_ids_dto(user_id=user_id,
                                                    role_ids=role_ids)
            for user_id, role_ids in user_id_and_role_ids_dict.items()
        ]
        return user_id_and_role_ids_dtos

    @staticmethod
    def _prepare_user_id_with_role_ids_dto(user_id, role_ids):
        from ib_iam.interactors.DTOs.common_dtos import UserIdWithRoleIdsDTO
        user_id_with_role_ids_dto = UserIdWithRoleIdsDTO(
            user_id=user_id,
            role_ids=role_ids
        )
        return user_id_with_role_ids_dto

    def get_valid_user_ids(self, user_ids: List[str]) -> List[str]:
        from ib_iam.models import UserDetails
        valid_user_ids = UserDetails.objects.filter(
            user_id__in=user_ids
        ).values_list("user_id", flat=True)
        return list(valid_user_ids)
