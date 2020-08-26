from typing import List

from ib_boards.adapters.iam_service import InvalidProjectIdsException, \
    UserIsNotInProjectException
from ib_boards.exceptions.custom_exceptions import InvalidProjectId


class ValidationMixin:

    def validate_given_project_ids(self, project_ids: List[str]):
        """
        @param project_ids:
        @type project_ids:
        @raise: InvalidProjectIdsException
        @rtype:
        """
        adapter = self.get_service_adapter()
        valid_project_ids = adapter.iam_service.validate_project_ids(
            project_ids)
        invalid_project_ids = [project_id for project_id in project_ids
                               if project_id not in valid_project_ids]
        if invalid_project_ids:
            raise InvalidProjectIdsException(invalid_project_ids)

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
        adapter = self.get_service_adapter()
        try:
            is_in_project = adapter.iam_service.validate_if_user_is_in_project(
                user_id=user_id, project_id=project_id)
        except InvalidProjectId:
            raise InvalidProjectIdsException([project_id])

        if not is_in_project:
            raise UserIsNotInProjectException

    @staticmethod
    def get_service_adapter():
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        return service_adapter
