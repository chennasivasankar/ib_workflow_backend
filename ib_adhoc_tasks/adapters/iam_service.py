class IamService:

    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_role_ids(self, user_id: str):
        user_role_ids = self.interface.get_user_role_ids(
            user_id=user_id
        )
        return user_role_ids
