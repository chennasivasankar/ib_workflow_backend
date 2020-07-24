from ib_tasks.interactors.storage_interfaces.create_or_update_task_storage_interface \
    import CreateOrUpdateTaskStorageInterface
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
    import GetTaskPresenterInterface
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException


class GetTaskInteractor:

    def __init__(self, storage: CreateOrUpdateTaskStorageInterface):
        self.storage = storage

    def get_task_wrapper(
            self, user_id: int, task_id: str,
            presenter: GetTaskPresenterInterface
    ):
        try:
            return self.get_task_response(user_id, task_id, presenter)
        except InvalidTaskIdException as err:
            return presenter.raise_exception_for_invalid_task_id(err)

    def get_task_response(
            self, user_id: int, task_id: str,
            presenter: GetTaskPresenterInterface
    ):
        task_details_dto = self.get_task(user_id, task_id)
        response = presenter.get_task_response(task_details_dto)
        return response

    def get_task(self, user_id: int, task_id: str):
        return self.storage.validate_task_id(task_id)
