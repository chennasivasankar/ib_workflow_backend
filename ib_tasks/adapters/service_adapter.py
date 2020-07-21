

class ServiceAdapter:

    @property
    def roles_service(self):
        from .roles_service import RolesService
        return RolesService()


def get_service_adapter():
    return ServiceAdapter()
