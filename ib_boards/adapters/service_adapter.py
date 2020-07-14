class ServiceAdapter:
    pass

    @property
    def task_service(self):
        from ib_boards.adapters.task_service import TaskService
        return TaskService()

    @property
    def user_service(self):
        from ib_boards.adapters.user_service import UserService
        return UserService()


def get_service_adapter():
    return ServiceAdapter()

