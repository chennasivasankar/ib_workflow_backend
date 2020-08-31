from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class UserNotAMemberOfAProject(Exception):
    pass


class ProjectRoleInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

    def get_user_role_ids_based_on_project(self, user_id: str, project_id: str):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        is_not_valid_project_id = not self.project_storage.is_valid_project_id(
            project_id=project_id
        )
        if is_not_valid_project_id:
            raise InvalidProjectId

        is_user_not_in_a_project = not self.project_storage.is_user_in_a_project(
            user_id=user_id, project_id=project_id
        )
        if is_user_not_in_a_project:
            raise UserNotAMemberOfAProject()

        role_ids = self.project_storage.get_user_role_ids(
            user_id=user_id, project_id=project_id
        )
        return role_ids
