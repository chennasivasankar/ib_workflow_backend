import abc


class AssignUserRolesForGivenProjectBulkPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_success_response_for_assign_user_roles_for_given_project(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_for_project(self, err):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_for_project(self, err):
        pass

    @abc.abstractmethod
    def response_for_invalid_project_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass
