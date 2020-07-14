class RolesServiceAdapter:

    @property
    def roles_service(self):
        from ib_tasks.adapters.roles_service import RolesService
        return RolesService()


def get_roles_service_adapter(self):
    return RolesServiceAdapter()
