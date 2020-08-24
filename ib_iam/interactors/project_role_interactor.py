from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class ProjectRoleInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

    def get_user_role_ids_based_on_project(self, user_id: str, project_id: str):
        '''
        TODO:
        Write Test cases
        validate user id
        validate project id
        '''
        role_ids = self.project_storage.get_user_role_ids(
            user_id=user_id, project_id=project_id
        )
        return role_ids
