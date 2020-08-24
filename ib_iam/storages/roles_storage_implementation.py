from typing import List

from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
from ib_iam.interactors.storage_interfaces.roles_storage_interface import \
    RolesStorageInterface


class RolesStorageImplementation(RolesStorageInterface):

    def create_roles(self, role_dtos: List[RoleDTO]):
        from ib_iam.models import ProjectRole
        role_objects = [
            ProjectRole(role_id=role_dto.role_id, name=role_dto.name,
                        description=role_dto.description)
            for role_dto in role_dtos]
        ProjectRole.objects.bulk_create(role_objects)

    def get_valid_role_ids(self, role_ids: List[str]):
        from ib_iam.models import ProjectRole
        valid_role_ids = ProjectRole.objects.filter(role_id__in=role_ids). \
            values_list("role_id", flat=True)
        return list(valid_role_ids)

    def validate_user_id(self, user_id):
        from ib_iam.models import UserDetails
        user_details_object = UserDetails.objects.filter(user_id=user_id)
        is_user_details_object_not_exist = not user_details_object.exists()
        if is_user_details_object_not_exist:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId

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
        from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
        user_id_with_role_ids_dto = UserIdWithRoleIdsDTO(
            user_id=user_id,
            role_ids=role_ids
        )
        return user_id_with_role_ids_dto

    def get_user_role_ids(self, user_id: str):
        from ib_iam.models import UserRole
        role_ids = UserRole.objects.filter(
            user_id=user_id
        ).values_list("role__role_id", flat=True)
        return list(role_ids)

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
