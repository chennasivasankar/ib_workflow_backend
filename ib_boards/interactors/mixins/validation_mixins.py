from typing import List


class ValidationMixin:

    def validate_given_project_ids(self, project_ids: List[str]):
        """
        @param project_ids:
        @type project_ids:
        @raise: InvalidProjectIdsException
        @rtype:
        """
        raise NotImplementedError

    def validate_if_user_is_in_project(self, user_id: str,
                                       project_id: str):
        """
        @param user_id:
        @type user_id:
        @param project_id:
        @type project_id:
        @raise: UserIsNotInProjectException
        @rtype:
        """
        raise NotImplementedError
