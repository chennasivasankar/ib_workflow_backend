from typing import List, Dict
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.interactors.task_template_dtos import TaskTemplateRolesDTO


class AddProjectAndRolesToTaskTemplatesInteractor:

    def __init__(self, task_template_storage: TaskTemplateStorageInterface):
        self.task_template_storage = task_template_storage

    def add_project_to_task_templates_interactor(
            self, project_id, task_template_ids: List[str]
    ):
        self._make_validations(
            project_id=project_id, task_template_ids=task_template_ids)

        existing_task_template_ids_of_project = self.task_template_storage.\
            get_existing_task_template_ids_of_project_task_templates(
                task_template_ids=task_template_ids, project_id=project_id)
        task_template_ids_to_create = [
            task_template_id
            for task_template_id in task_template_ids
            if task_template_id not in existing_task_template_ids_of_project
        ]

        self.task_template_storage.add_project_to_task_templates(
            project_id=project_id,
            task_template_ids=task_template_ids_to_create)

    def add_roles_to_task_templates(
            self, task_template_role_dtos: List[TaskTemplateRolesDTO]):
        task_template_ids = \
            self._get_task_template_ids_of_task_template_roles_dtos(
                task_template_role_dtos=task_template_role_dtos)
        self._validate_task_template_ids(task_template_ids=task_template_ids)

        self._validate_role_ids_of_task_template_role_dtos(
            task_template_role_dtos=task_template_role_dtos)

        existing_task_template_role_dtos = self.task_template_storage.\
            get_existing_role_dtos_of_task_templates(
                task_template_ids=task_template_ids)
        existing_roles_of_task_templates_dict = \
            self._make_roles_of_task_templates_dict(
                task_template_role_dtos=existing_task_template_role_dtos)

        task_template_role_dtos_to_create = \
            self._get_task_template_role_dtos_to_create(
                task_template_role_dtos=task_template_role_dtos,
                existing_roles_of_task_templates_dict=
                existing_roles_of_task_templates_dict)

        self.task_template_storage.create_task_template_permitted_roles(
            task_template_role_dtos=task_template_role_dtos_to_create
        )

    def _validate_role_ids_of_task_template_role_dtos(
            self, task_template_role_dtos: List[TaskTemplateRolesDTO]):
        for task_template_role_dto in task_template_role_dtos:
            role_ids = task_template_role_dto.role_ids
            self._validate_duplicate_role_ids_for_template(
                role_ids=role_ids,
                task_template_id=task_template_role_dto.task_template_id)

        role_ids = self._get_role_ids_of_task_template_role_dtos(
            task_template_role_dtos=task_template_role_dtos)

        from ib_tasks.adapters.roles_service import RolesService
        role_service = RolesService()
        valid_role_ids = role_service.get_valid_role_ids_in_given_role_ids(
            role_ids=role_ids)

        invalid_role_ids = [
            role_id for role_id in role_ids if role_id not in valid_role_ids
        ]
        if invalid_role_ids:
            from ib_tasks.exceptions.roles_custom_exceptions import \
                InvalidRoleIdsException
            raise InvalidRoleIdsException(role_ids=invalid_role_ids)

    def _make_validations(self, project_id: str, task_template_ids: List[str]):
        self._validate_task_template_ids(task_template_ids=task_template_ids)

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        project_id_list = [project_id]
        valid_project_ids = \
            service_adapter.project_service.get_valid_project_ids(
                project_ids=project_id_list)
        is_invalid_project = not valid_project_ids
        if is_invalid_project:
            from ib_tasks.exceptions.custom_exceptions import \
                InvalidProjectId
            raise InvalidProjectId(project_id)

    def _validate_task_template_ids(self, task_template_ids: List[str]):

        import collections
        task_template_ids_counter = collections.Counter(task_template_ids)
        duplicate_task_template_ids = [
            task_template_id
            for task_template_id, count in task_template_ids_counter.items()
            if count > 1
        ]

        if duplicate_task_template_ids:
            from ib_tasks.exceptions.custom_exceptions import \
                DuplicateTaskTemplateIdsGivenToAProject
            raise DuplicateTaskTemplateIdsGivenToAProject(
                duplicate_task_template_ids)

        valid_task_template_ids = self.task_template_storage. \
            get_valid_task_template_ids_in_given_task_template_ids(
                template_ids=task_template_ids)
        invalid_task_template_ids = [
            task_template_id for task_template_id in task_template_ids
            if task_template_id not in valid_task_template_ids
        ]

        if invalid_task_template_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskTemplateIds
            raise InvalidTaskTemplateIds(invalid_task_template_ids)

    @staticmethod
    def _get_task_template_ids_of_task_template_roles_dtos(
            task_template_role_dtos: List[TaskTemplateRolesDTO]) -> List[str]:
        task_template_ids = [
            task_template_role_dto.task_template_id
            for task_template_role_dto in task_template_role_dtos
        ]
        return task_template_ids

    @staticmethod
    def _get_role_ids_of_task_template_role_dtos(
            task_template_role_dtos: List[TaskTemplateRolesDTO]) -> List[str]:
        role_ids = []
        for task_template_role_dto in task_template_role_dtos:
            role_ids += task_template_role_dto.role_ids
        return role_ids

    @staticmethod
    def _validate_duplicate_role_ids_for_template(
            task_template_id: str, role_ids: List[str]):
        import collections
        role_ids_counter = collections.Counter(role_ids)
        duplicate_role_ids = [
            role_id for role_id, count in role_ids_counter.items()
            if count > 1
        ]

        if duplicate_role_ids:
            from ib_tasks.exceptions.custom_exceptions import \
                DuplicateRoleIdsGivenToATaskTemplate
            raise DuplicateRoleIdsGivenToATaskTemplate(
                task_template_id=task_template_id, role_ids=role_ids)

    @staticmethod
    def _make_roles_of_task_templates_dict(
            task_template_role_dtos: List[TaskTemplateRolesDTO]) -> Dict:
        role_ids_group_by_task_template_ids = {}
        for task_template_role_dto in task_template_role_dtos:
            role_ids_group_by_task_template_ids[
                task_template_role_dto.task_template_id
            ] = task_template_role_dto.role_ids
        return role_ids_group_by_task_template_ids

    @staticmethod
    def _get_task_template_role_dtos_to_create(
            task_template_role_dtos: List[TaskTemplateRolesDTO],
            existing_roles_of_task_templates_dict: Dict
    ) -> List[TaskTemplateRolesDTO]:
        task_template_role_dtos_to_create = []
        for task_template_role_dto in task_template_role_dtos:
            is_template_having_roles = \
                task_template_role_dto.task_template_id in \
                existing_roles_of_task_templates_dict.keys()

            existing_roles_of_task_template = []
            if is_template_having_roles:
                existing_roles_of_task_template = \
                    existing_roles_of_task_templates_dict[
                        task_template_role_dto.task_template_id]

            role_ids_to_create = [
                role_id for role_id in task_template_role_dto.role_ids
                if role_id not in existing_roles_of_task_template
            ]

            if role_ids_to_create:
                task_template_role_dtos_to_create.append(
                    TaskTemplateRolesDTO(
                        task_template_id=
                        task_template_role_dto.task_template_id,
                        role_ids=role_ids_to_create
                    )
                )
        return task_template_role_dtos_to_create
