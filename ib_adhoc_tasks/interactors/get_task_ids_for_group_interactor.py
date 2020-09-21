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
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_role_ids = service.iam_service.get_user_role_ids_based_on_project(
            user_id=task_ids_for_groups_parameter_dto.user_id,
            project_id=task_ids_for_groups_parameter_dto.project_id
        )
        stage_ids = service.task_service.get_stage_ids_based_on_user_roles(
            user_role_ids=user_role_ids
        )
        task_ids_and_count_dto = self.elastic_storage. \
            get_task_ids_and_count_dto_based_on_given_groupby_and_pagination_detail(
            task_ids_for_groups_parameter_dto=task_ids_for_groups_parameter_dto,
            stage_ids=stage_ids
        )
        return task_ids_and_count_dto

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        valid_project_ids = service.iam_service.get_valid_project_ids(
            project_ids=[project_id])
        is_invalid_project = (
                valid_project_ids == [] or project_id not in valid_project_ids
        )
        if is_invalid_project:
            from ib_adhoc_tasks.exceptions.custom_exceptions import \
                InvalidProjectId
            raise InvalidProjectId

    @staticmethod
    def _validate_template_id(template_id: str):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        service.task_service.validate_task_template_id(
            task_template_id=template_id
        )
