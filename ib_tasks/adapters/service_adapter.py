class ServiceAdapter:

    @property
    def roles_service(self):
        from .roles_service import RolesService
        return RolesService()

    @property
    def auth_service(self):
        from ib_tasks.adapters.auth_service import AuthService
        return AuthService()


def get_service_adapter():
    return ServiceAdapter()
