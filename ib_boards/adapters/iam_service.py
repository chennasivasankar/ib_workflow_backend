class IamService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_roles(self, user_id: str):

        pass
