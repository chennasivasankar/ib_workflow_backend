from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
    DeleteUserStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import UserDTO
from ib_iam.models import UserDetails, UserRole, TeamUser


class DeleteUserStorageImplementation(DeleteUserStorageInterface):
    def delete_user(self, user_id: str):
        UserDetails.objects.filter(user_id=user_id).delete()

    def delete_user_roles(self, user_id: str):
        UserRole.objects.filter(user_id=user_id).delete()

    def delete_user_teams(self, user_id: str):
        TeamUser.objects.filter(user_id=user_id).delete()

    def get_user_details(self, user_id: str) -> UserDTO:
        try:
            user_object = UserDetails.objects.get(user_id=user_id)
        except UserDetails.DoesNotExist:
            from ib_iam.exceptions.custom_exceptions import UserNotFound
            raise UserNotFound
        else:
            return UserDTO(
                user_id=user_object.user_id,
                is_admin=user_object.is_admin,
                company_id=str(user_object.company_id)
            )
