class ServiceAdapter:

    @property
    def roles_service(self):
        from .roles_service import RolesService
        return RolesService()

    @property
    def auth_service(self):
        from ib_tasks.adapters.auth_service import AuthService
        return AuthService()

    @property
    def boards_service(self):
        from .boards_service import BoardsService
        return BoardsService()

    @property
    def assignee_details_service(self):
        from ib_tasks.adapters.assignees_details_service import \
            AssigneeDetailsService
        return AssigneeDetailsService()

    @property
    def search_service(self):
        from .search_service import SearchService
        return SearchService()

    @property
    def searchable_details_service(self):
        from .searchable_details_service import SearchableDetailsService
        return SearchableDetailsService()


def get_service_adapter():
    return ServiceAdapter()
