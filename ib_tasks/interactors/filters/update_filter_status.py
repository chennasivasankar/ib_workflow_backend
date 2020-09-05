"""
Created on: 03/09/20
Author: Pavankumar Pamuru

"""

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface \
    import \
    FilterPresenterInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface


class UpdateFilerStatusInteractor(ValidationMixin):

    def __init__(
            self, filter_storage: FilterStorageInterface,
            presenter: FilterPresenterInterface):
        self.presenter = presenter
        self.filter_storage = filter_storage

    def update_filter_select_status_wrapper(
            self, user_id: str, filter_id: int, filter_status: Status):
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        from ib_tasks.exceptions.filter_exceptions \
            import UserNotHaveAccessToFilter
        try:
            response = self.update_filter_select_status(
                user_id=user_id, filter_id=filter_id, is_selected=filter_status
            )
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return self.presenter \
                .get_response_for_invalid_user_to_update_filter_status()
        return self.presenter.get_response_for_update_filter_status(
            filter_id=filter_id, filter_status=response
        )

    def update_filter_select_status(
            self, user_id: str, filter_id: int, is_selected: Status):

        self.validate_filter_id(filter_id=filter_id)
        self.validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )
        response = self.filter_storage.update_filter_status(
            filter_id=filter_id, is_selected=is_selected
        )
        return response
