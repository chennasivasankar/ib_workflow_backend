from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
    DeleteUserStorageInterface
from ib_iam.interactors.storage_interfaces.dtos import UserDTO


class DeleteUserStorageImplementation(DeleteUserStorageInterface):
    def delete_user(self, user_id: str):
        pass

    def delete_user_roles(self, user_id: str):
        pass

    def delete_user_teams(self, user_id: str):
        pass

    def check_is_admin_user(self, user_id: str) -> bool:
        from ib_iam.models import UserDetails
        return UserDetails.objects.get(user_id=user_id).is_admin

    def get_user_details(self, user_id: str) -> UserDTO:
        pass
