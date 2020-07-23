

class ServiceAdapter:

    @property
    def roles_service(self):
        from .roles_service import RolesService
        return RolesService()

    @property
    def boards_service(self):
        from .boards_service import BoardsService
        return BoardsService()


def get_service_adapter():
    return ServiceAdapter()
