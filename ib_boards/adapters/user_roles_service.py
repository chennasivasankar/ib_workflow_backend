

class UserRolesService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_roles(self, user_id: str):
        list_of_user_roles = self.interface.get_user_roles_list(user_id=user_id)
        list_of_user_roles = list_of_user_roles

        return list_of_user_roles