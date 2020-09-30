from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.dtos.dtos import TasksDetailsInputDTO
from ib_tasks.interactors.get_task_details_interactor import \
    GetTaskDetailsInteractor
from ib_tasks.interactors.get_task_fields_and_actions import \
    GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import \
    FieldDisplayNameDTO, FieldNameDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO, TaskStagesDTO, StageDisplayNameValueDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    SubTasksCountDTO, \
    SubTasksIdsDTO, TaskProjectDTO, TaskDisplayIdDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO, \
    TaskDetailsConfigDTO, TaskWithCompletedSubTasksCountDTO
from ib_tasks.interactors.task_stage_dtos import TasksCompleteDetailsDTO
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ib_tasks.storages.gof_storage_implementation import \
    GoFStorageImplementation
from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation
from ib_tasks.storages.task_stage_storage_implementation import \
    TaskStageStorageImplementation
from ib_tasks.storages.task_template_storage_implementation import \
    TaskTemplateStorageImplementation
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation


class ServiceInterface:

    @staticmethod
    def get_task_ids_for_the_stages(
            task_config_dtos: List[TaskDetailsConfigDTO]):
        from ib_tasks.interactors.get_task_ids_interactor import \
            GetTaskIdsInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        from ib_tasks.storages.elasticsearch_storage_implementation import \
            ElasticSearchStorageImplementation
        elasticsearch_storage = ElasticSearchStorageImplementation()
        from ib_tasks.storages.filter_storage_implementation import \
            FilterStorageImplementation
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        field_storage = FieldsStorageImplementation()
        filter_storage = FilterStorageImplementation()
        interactor = GetTaskIdsInteractor(
            task_storage=TasksStorageImplementation(),
            stage_storage=StagesStorageImplementation(),
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage,
            field_storage=field_storage
        )

        task_ids_dtos = interactor.get_task_ids(
            task_details_configs=task_config_dtos
        )
        return task_ids_dtos

    @staticmethod
    def get_task_details(task_dtos: List[GetTaskDetailsDTO], user_id: str,
                         view_type: ViewType) -> \
            List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        field_storage = FieldsStorageImplementation()
        stage_storage = StagesStorageImplementation()
        action_storage = ActionsStorageImplementation()
        task_storage = TasksStorageImplementation()

        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage=field_storage,
            stage_storage=stage_storage,
            action_storage=action_storage,
            task_storage=task_storage,
        )
        result = interactor.get_task_fields_and_action(task_dtos, user_id,
                                                       view_type)
        return result

    @staticmethod
    def get_assignees_for_task_stages(
            task_stage_dtos: List[GetTaskDetailsDTO], project_id: str
    ) -> List[TaskStageAssigneeTeamDetailsDTO]:
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import \
            GetStagesAssigneesDetailsInteractor
        from ib_tasks.storages.task_stage_storage_implementation import \
            TaskStageStorageImplementation
        assignees_interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=TaskStageStorageImplementation()
        )
        return \
            assignees_interactor.get_stages_assignee_details_by_given_task_ids(
                task_stage_dtos=task_stage_dtos, project_id=project_id
            )

    @staticmethod
    def validate_stage_ids_with_template_id(
            template_stages: List[TaskStagesDTO]):
        from ib_tasks.interactors.basic_validations_interactor import \
            BasicValidationsInteractor
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        interactor = BasicValidationsInteractor(
            storage=StagesStorageImplementation()
        )
        interactor.validate_stages_with_task_template_ids(
            template_stages=template_stages
        )

    @staticmethod
    def validate_task_template_ids(task_template_ids: List[str]):
        from ib_tasks.interactors.basic_validations_interactor import \
            BasicValidationsInteractor
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        interactor = BasicValidationsInteractor(
            storage=StagesStorageImplementation()
        )
        return interactor.validate_template_ids(template_ids=task_template_ids)

    @staticmethod
    def get_field_display_names(
            field_ids: List[str], user_id: str,
            project_id: str) -> List[FieldDisplayNameDTO]:
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        field_storage = FieldsStorageImplementation()
        from ib_tasks.interactors.get_field_display_name import \
            GetFieldDisplayNamesInteractor
        interactor = GetFieldDisplayNamesInteractor(
            field_storage=field_storage
        )
        return interactor.get_field_display_names(
            user_id=user_id,
            field_ids=field_ids,
            project_id=project_id
        )

    @staticmethod
    def get_user_permitted_stage_ids(
            user_roles: List[str]
    ) -> List[str]:
        from ib_tasks.interactors.get_user_permitted_stage_ids \
            import GetUserPermittedStageIds
        stage_storage = StagesStorageImplementation()
        interactor = GetUserPermittedStageIds(stage_storage=stage_storage)
        stage_ids = interactor.get_permitted_stage_ids_to_user_role_ids(
            user_roles=user_roles
        )
        return stage_ids

    @staticmethod
    def get_stage_details(stage_ids: List[str]) -> List[StageDisplayNameValueDTO]:
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        from ib_tasks.interactors.get_stage_details import GetStageDetails
        interactor = GetStageDetails(storage)
        stage_details_dtos = interactor.get_stage_details(stage_ids=stage_ids)
        return stage_details_dtos

    @staticmethod
    def get_tasks_complete_details(
            input_dto: TasksDetailsInputDTO
    ) -> TasksCompleteDetailsDTO:
        from ib_tasks.interactors.get_tasks_complete_details_interactor \
            import GetTasksCompleteDetailsInteractor
        task_storage = TasksStorageImplementation()
        action_storage = ActionsStorageImplementation()
        task_stage_storage = TaskStageStorageImplementation()
        stage_storage = StagesStorageImplementation()
        field_storage = FieldsStorageImplementation()
        interactor = GetTasksCompleteDetailsInteractor(
            task_storage=task_storage,
            action_storage=action_storage,
            stage_storage=stage_storage,
            field_storage=field_storage,
            task_stage_storage=task_stage_storage
        )
        response = interactor.get_tasks_complete_details(input_dto=input_dto)
        return response

    @staticmethod
    def get_sub_tasks_count_task_ids(task_ids: List[int]) -> \
            List[SubTasksCountDTO]:
        task_storage = TasksStorageImplementation()
        from ib_tasks.interactors.sub_tasks_interactor import \
            SubTasksInteractor
        interactor = SubTasksInteractor(task_storage=task_storage)
        sub_tasks_count_dtos = interactor.get_sub_tasks_count_task_ids(
            task_ids=task_ids
        )
        return sub_tasks_count_dtos

    @staticmethod
    def get_sub_task_ids_to_task_ids(task_ids: List[int]) -> \
            List[SubTasksIdsDTO]:
        task_storage = TasksStorageImplementation()
        from ib_tasks.interactors.sub_tasks_interactor import \
            SubTasksInteractor
        interactor = SubTasksInteractor(task_storage=task_storage)
        task_id_with_sub_task_ids_dtos = \
            interactor.get_sub_task_ids_to_task_ids(
                task_ids=task_ids
            )
        return task_id_with_sub_task_ids_dtos

    @staticmethod
    def get_tasks_project_ids(task_ids: List[int]) -> List[TaskProjectDTO]:
        task_storage = TasksStorageImplementation()
        interactor = GetTaskDetailsInteractor(task_storage)
        return interactor.get_task_project_ids(task_ids)

    @staticmethod
    def get_task_ids_for_given_task_display_ids(task_display_ids: List[str]) \
            -> List[TaskDisplayIdDTO]:
        task_storage = TasksStorageImplementation()
        interactor = GetTaskDetailsInteractor(task_storage)
        return interactor.get_task_ids_for_given_task_display_ids(
            task_display_ids)

    @staticmethod
    def get_tasks_completed_sub_tasks_count_dtos(
            task_ids: List[int]
    ) -> List[TaskWithCompletedSubTasksCountDTO]:
        from ib_tasks.interactors.get_tasks_completed_sub_tasks_count import \
            GetTasksCompletedSubTasksCount
        task_storage = TasksStorageImplementation()
        task_stage_storage = TaskStageStorageImplementation()
        interactor = GetTasksCompletedSubTasksCount(
            task_stage_storage=task_stage_storage,
            task_storage=task_storage
        )
        task_with_completed_sub_tasks_count_dtos = \
            interactor.get_tasks_completed_sub_tasks_count(
                task_ids=task_ids
            )
        return task_with_completed_sub_tasks_count_dtos

    def get_task_template_field_dtos(
            self, user_id: str, project_ids: List[str], template_id: str
    ) -> List[FieldNameDTO]:
        # TODO need to write test cases
        from ib_tasks.interactors.get_templates_fields_to_project_ids import \
            GetProjectsTemplatesFieldsInteractor
        task_template_storage = TaskTemplateStorageImplementation()
        gof_storage = GoFStorageImplementation()
        field_storage = FieldsStorageImplementation()
        interactor = GetProjectsTemplatesFieldsInteractor(
            task_template_storage=task_template_storage,
            gof_storage=gof_storage,
            field_storage=field_storage
        )

        return interactor.get_task_template_field_dtos(
            user_id=user_id, project_ids=project_ids, template_id=template_id
        )
