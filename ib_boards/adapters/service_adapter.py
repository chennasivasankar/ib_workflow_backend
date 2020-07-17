class ServiceAdapter:
    @property
    def task_service(self):
        from .tasks_service import TaskService
        return TaskService()

    @property
    def user_roles_service(self):
        from .user_roles_service import UserRolesService
        return UserRolesService()

def get_service_adapter():
    return ServiceAdapter()