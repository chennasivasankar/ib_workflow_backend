"""
Created on: 03/09/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException, \
    UserIsNotInProjectException
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO, FilterDTO
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import \
    FilterPresenterInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface


class GetFiltersInteractor(ValidationMixin):
    def __init__(
            self, filter_storage: FilterStorageInterface,
            presenter: FilterPresenterInterface):
        self.presenter = presenter
        self.filter_storage = filter_storage

    def get_filters_details_wrapper(self, user_id: str, project_id: str):

        try:
            filter_details = self.get_filters_details(
                user_id=user_id, project_id=project_id
            )
        except InvalidProjectIdsException as err:
            return self.presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return self.presenter.get_response_for_user_not_in_project()
        return self.presenter.get_response_for_get_filters_details(
            filter_complete_details=filter_details
        )

    def get_filters_details(self, user_id: str, project_id: str):

        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )
        filters_dto = self.filter_storage.get_filters_dto_to_user(
            user_id=user_id, project_id=project_id
        )
        filter_ids = self._get_filter_ids(filters_dto)
        conditions_dto = \
            self.filter_storage.get_conditions_to_filters(
                filter_ids=filter_ids)
        filter_complete_details_dto = FilterCompleteDetailsDTO(
            filters_dto=filters_dto,
            conditions_dto=conditions_dto
        )
        return filter_complete_details_dto

    @staticmethod
    def _get_filter_ids(filters_dto: List[FilterDTO]):

        return [
            filter_dto.filter_id
            for filter_dto in filters_dto
        ]
