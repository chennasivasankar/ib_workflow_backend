from typing import List

from ib_iam.exceptions.custom_exceptions import UserDoesNotExist
from ib_iam.interactors.presenter_interfaces.project_presenter_interface import \
    GetProjectBriefInfoPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectWithDisplayIdDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetProjectBriefInfoInteractor:

    def __init__(
            self, project_storage: ProjectStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.project_storage = project_storage
        self.user_storage = user_storage

    def get_project_brief_info_wrapper(
            self, user_id: str,
            presenter: GetProjectBriefInfoPresenterInterface
    ):
        try:
            response = self._get_project_brief_info_response(
                user_id=user_id, presenter=presenter
            )
        # except InvalidOffsetValue:
        #     response = presenter.response_for_invalid_offset()
        # except InvalidLimitValue:
        #     response = presenter.response_for_invalid_limit()
        except UserDoesNotExist:
            response = presenter.response_for_user_does_not_exist()
        return response

    def _get_project_brief_info_response(
            self, user_id: str,
            presenter: GetProjectBriefInfoPresenterInterface
    ):
        project_dtos = self.get_project_brief_info(
            user_id=user_id
        )
        response = presenter.success_response_for_get_project_brief_info(
            project_dtos=project_dtos
        )
        return response

    def get_project_brief_info(
            self, user_id: str
    ) -> List[ProjectWithDisplayIdDTO]:
        # self._validate_limit_and_offset(
        #     pagination_dto=pagination_dto
        # )
        is_user_not_exists = not self.user_storage.is_user_exist(
            user_id=user_id)
        if is_user_not_exists:
            raise UserDoesNotExist
        project_dtos = self.project_storage.get_user_project_dtos(
            user_id=user_id
        )
        return project_dtos

    # def _validate_limit_and_offset(
    #         self, pagination_dto: PaginationDTO
    # ):
    #     self._validate_offset(pagination_dto.offset)
    #     self._validate_limit(pagination_dto.limit)
    #
    # @staticmethod
    # def _validate_offset(offset):
    #     is_invalid_offset = offset < 0
    #     if is_invalid_offset:
    #         raise InvalidOffsetValue
    #
    # @staticmethod
    # def _validate_limit(limit):
    #     is_invalid_limit = limit < 0
    #     if is_invalid_limit:
    #         raise InvalidLimitValue
