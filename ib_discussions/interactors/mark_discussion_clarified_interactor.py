from ib_discussions.exceptions.custom_exceptions import DiscussionIdNotFound, \
    UserCannotMarkAsClarified
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    MarkDiscussionClarifiedPresenterInterface
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class MarkDiscussionClarifiedInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def mark_discussion_clarified_wrapper(
            self, discussion_id: str, user_id: str,
            presenter: MarkDiscussionClarifiedPresenterInterface
    ):
        try:
            response = self._mark_discussion_clarified_response(
                discussion_id=discussion_id, user_id=user_id,
                presenter=presenter
            )
        except DiscussionIdNotFound:
            response = presenter.raise_exception_for_discussion_id_not_found()
        except UserCannotMarkAsClarified:
            response \
                = presenter.raise_exception_for_user_cannot_mark_as_clarified()
        return response

    def _mark_discussion_clarified_response(
            self, discussion_id: str, user_id: str,
            presenter: MarkDiscussionClarifiedPresenterInterface
    ):
        self.mark_discussion_clarified(
            discussion_id=discussion_id, user_id=user_id
        )
        return \
            presenter.raise_success_response_for_mark_discussion_as_clarified()

    def mark_discussion_clarified(self, discussion_id: str, user_id: str):
        self.storage.validate_discussion_id(discussion_id=discussion_id)
        self.storage.validate_is_user_can_mark_as_clarified(
            user_id=user_id, discussion_id=discussion_id
        )
        self.storage.mark_discussion_clarified(discussion_id=discussion_id)
        return
            

