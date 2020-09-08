from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
    CreateChecklistItemPresenterInterface
)


class CreateChecklistItemPresenterImplementation(
    CreateChecklistItemPresenterInterface, HTTPResponseMixin
):

    def get_response_for_create_checklist_item(
            self, checklist_item_id: str
    ):
        return self.prepare_201_created_response(
            response_dict={"checklist_item_id": checklist_item_id}
        )
