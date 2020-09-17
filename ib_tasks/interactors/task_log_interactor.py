from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.task_dtos import CreateTaskLogDTO


class TaskLogInteractor:
    def __init__(
            self, task_storage: TaskStorageInterface,
            storage: StorageInterface,
            action_storage: ActionStorageInterface
    ):
        self.action_storage = action_storage
        self.task_storage = task_storage
        self.storage = storage

    def create_task_log(
            self, create_task_log_dto: CreateTaskLogDTO):
        self._make_validations(create_task_log_dto=create_task_log_dto)

        self.task_storage.create_task_log(
            create_task_log_dto=create_task_log_dto)

    def _make_validations(self, create_task_log_dto: CreateTaskLogDTO):
        self._validate_task_json_string(
            task_json=create_task_log_dto.task_json)
        is_task_exists = self.task_storage.check_is_task_exists(
            task_id=create_task_log_dto.task_id)
        is_task_not_exists = not is_task_exists
        if is_task_not_exists:
            from ib_tasks.exceptions.task_custom_exceptions import \
                TaskDoesNotExists
            from ib_tasks.constants.exception_messages import INVALID_TASK_ID
            raise TaskDoesNotExists(
                INVALID_TASK_ID[0].format(create_task_log_dto.task_id)
            )
        is_action_exists = self.action_storage.validate_action(
            action_id=create_task_log_dto.action_id
        )
        is_action_not_exists = not is_action_exists
        if is_action_not_exists:
            from ib_tasks.exceptions.action_custom_exceptions import \
                ActionDoesNotExists
            from ib_tasks.constants.exception_messages import \
                INVALID_ACTION_ID
            raise ActionDoesNotExists(INVALID_ACTION_ID[0].format(
                create_task_log_dto.action_id)
            )

    @staticmethod
    def _validate_task_json_string(task_json: str):
        task_json_after_strip = task_json.strip()
        is_task_json_empty = not task_json_after_strip
        if is_task_json_empty:
            from ib_tasks.constants.exception_messages \
                import INVALID_TASK_JSON
            from ib_tasks.exceptions.task_custom_exceptions \
                import InvalidTaskJson
            raise InvalidTaskJson(INVALID_TASK_JSON)
