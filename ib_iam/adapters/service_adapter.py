class ServiceAdapter:

    @property
    def user_service(self):
        from ib_iam.adapters.user_service import UserService
        return UserService()


def get_service_adapter():
    return ServiceAdapter()
