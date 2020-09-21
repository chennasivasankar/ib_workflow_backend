from ib_adhoc_tasks.interactors.dtos import TaskIdsForGroupsParameterDTO, \
    TaskIdsAndCountDTO
from ib_adhoc_tasks.interactors.storage_interfaces \
    .elastic_storage_interface import ElasticStorageInterface


class GetTaskIdsForGroupInteractor:

    def __init__(self, elastic_storage: ElasticStorageInterface):
        self.elastic_storage = elastic_storage

    def get_task_ids_for_groups(
            self,
            task_ids_for_groups_parameter_dto: TaskIdsForGroupsParameterDTO,
    ) -> TaskIdsAndCountDTO:
        self._validate_project_id(
            project_id=task_ids_for_groups_parameter_dto.project_id)
        self._validate_template_id(
            template_id=task_ids_for_groups_parameter_dto.template_id)
        from ib_adhoc_tasks.adapters.iam_service import IAMService
        iam_service = IAMService()
        user_role_ids = iam_service.get_user_role_ids_based_on_project(
            user_id=task_ids_for_groups_parameter_dto.user_id,
            project_id=task_ids_for_groups_parameter_dto.project_id
        )
        from ib_adhoc_tasks.adapters.task_service import TaskService
        task_service = TaskService()
        stage_ids = task_service.get_stage_ids_based_on_user_roles(
            user_role_ids=user_role_ids
        )
        task_ids_and_count_dto = self.elastic_storage. \
            get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto,
            stage_ids=stage_ids
        )
        return task_ids_and_count_dto

    def _validate_project_id(self, project_id: str):
        from ib_adhoc_tasks.adapters.iam_service import IAMService
        iam_service = IAMService()
        is_project_exists = iam_service.is_project_exists(
            project_id=project_id
        )
        is_project_not_exists = not is_project_exists
        if is_project_not_exists:
            from ib_adhoc_tasks.exceptions.custom_exceptions import \
                InvalidProjectId
            raise InvalidProjectId

    def _validate_template_id(self, template_id: str):
        from ib_adhoc_tasks.adapters.task_service import TaskService
        task_service = TaskService()
        is_template_exists = task_service.is_template_exists(
            template_id=template_id
        )
        is_template_not_exists = not is_template_exists
        if is_template_not_exists:
            from ib_adhoc_tasks.exceptions.custom_exceptions import \
                InvalidTemplateId
            raise InvalidTemplateId
