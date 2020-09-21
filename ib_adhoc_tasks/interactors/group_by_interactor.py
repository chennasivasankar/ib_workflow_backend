from ib_adhoc_tasks.interactors.presenter_interfaces \
    .get_group_by_presenter_interface import GetGroupByPresenterInterface
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GroupByInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_group_by_wrapper(
            self, project_id: str, user_id: str,
            presenter: GetGroupByPresenterInterface
    ):
        group_by_response_dtos = self.get_group_by(
            project_id=project_id, user_id=user_id
        )
        return presenter.get_response_for_get_group_by(
            group_by_response_dtos=group_by_response_dtos
        )

    def get_group_by(self, project_id: str, user_id: str):
        group_by_response_dtos = self.storage.get_group_by_dtos(user_id=user_id)
        return group_by_response_dtos
