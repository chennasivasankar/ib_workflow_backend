from abc import ABC, abstractmethod


class AssignUserRolesForGivenProjectBulkPresenterInterface(ABC):

    @abstractmethod
    def prepare_success_response_for_assign_user_roles_for_given_project(self):
        pass

    @abstractmethod
    def response_for_invalid_user_ids_for_project(self, err):
        pass

    @abstractmethod
    def response_for_invalid_role_ids_for_project(self, err):
        pass

    @abstractmethod
    def response_for_invalid_project_id(self):
        pass
