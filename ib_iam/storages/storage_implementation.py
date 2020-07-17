from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):
    def get_is_admin_of_given_user_id(self, user_id: int):
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)
        is_admin = user_object.is_admin
        return is_admin
