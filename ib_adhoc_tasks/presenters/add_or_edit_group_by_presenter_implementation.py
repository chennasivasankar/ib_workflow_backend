from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_adhoc_tasks.interactors.presenter_interfaces \
    .group_by_presenter_interface import AddOrEditGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO


class AddOrEditGroupByPresenterImplementation(
    AddOrEditGroupByPresenterInterface, HTTPResponseMixin
):

    def get_response_for_add_or_edit_group_by(
            self, group_by_response_dto: GroupByResponseDTO
    ):
        group_by_response_dictionary = self._convert_to_group_by_response_dict(
            group_by_response_dto=group_by_response_dto
        )
        return self.prepare_200_success_response(
            response_dict=group_by_response_dictionary
        )

    @staticmethod
    def _convert_to_group_by_response_dict(
            group_by_response_dto: GroupByResponseDTO
    ):
        return {
            "group_by_id": group_by_response_dto.group_by_id,
            "group_by_display_name":
                group_by_response_dto.group_by_display_name,
            "order": group_by_response_dto.order
        }
