from typing import List, Tuple, Union, Optional, Dict

from ib_tasks.adapters.dtos import UserDetailsDTO, AssigneeDetailsDTO
from ib_tasks.adapters.dtos import UserIdWIthTeamDetailsDTO
from ib_tasks.adapters.service_adapter import get_service_adapter, \
    ServiceAdapter
from ib_tasks.interactors.stages_dtos import StageWithUserDetailsDTO, \
    StageWithUserDetailsAndTeamDetailsDTO, StageIdWithNameDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos \
    import StageDetailsDTO, AssigneeCurrentTasksCountDTO, \
    StageIdWithRoleIdsDTO, TaskWithDbStageIdDTO, StageRoleDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import TaskStageStorageInterface


class GetUsersWithLessTasksInGivenStagesInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.stage_storage = stage_storage
        self.action_storage = action_storage
        self.task_stage_storage = task_stage_storage

    def get_users_with_less_tasks_in_given_stages(
            self, stage_ids: List[str],
            project_id: str,
            task_id: int) -> StageWithUserDetailsAndTeamDetailsDTO:

        stage_detail_dtos = self.stage_storage. \
            get_stage_detail_dtos_given_stage_ids(stage_ids=stage_ids)
        db_stage_ids = self._get_db_stage_ids_given_stage_detail_dtos(
            stage_detail_dtos)

        service_adapter = get_service_adapter()
        project_service = service_adapter.project_service
        projects_config = project_service.get_projects_config()

        stage_assignee_details = self._assign_created_user_or_random_users(
            db_stage_ids, project_id, task_id, projects_config,
            stage_detail_dtos, service_adapter)
        stage_with_user_details_and_team_details_dto = self. \
            _get_stage_with_user_details_and_team_details_dto(
            stages_with_user_details_dtos=stage_assignee_details,
            project_id=project_id)

        return stage_with_user_details_and_team_details_dto

    def _assign_created_user_or_random_users(
            self, db_stage_ids: List[int], project_id: str,
            task_id: int, projects_config: Dict,
            stage_detail_dtos: List[StageDetailsDTO],
            service_adapter: ServiceAdapter
    ) -> List[StageWithUserDetailsDTO]:
        project_config = projects_config.get(project_id)
        given_project_has_config = project_config is not None

        if given_project_has_config:
            assignee_restriction_is_true = project_config.get("restrict_assignee_to_user")
            if assignee_restriction_is_true:
                return self._stage_assignee_details_of_created_user(
                    stage_detail_dtos, task_id, service_adapter)

        stages_assignee_details = self. \
            _get_previous_user_or_user_having_less_tasks_details_dtos_for_given_stages(
            db_stage_ids=db_stage_ids, stage_detail_dtos=stage_detail_dtos,
            project_id=project_id, task_id=task_id)
        return stages_assignee_details

    def _stage_assignee_details_of_created_user(
            self, stage_details_dtos: List[StageDetailsDTO],
            task_id: int, service_adapter: ServiceAdapter
    ) -> List[StageWithUserDetailsDTO]:
        task_created_user_id = \
            self.task_stage_storage.get_task_created_by_id(task_id)
        assignee_details_service = service_adapter.assignee_details_service
        user_details_dto = assignee_details_service.get_assignees_details_dtos(
            [task_created_user_id])[0]
        stage_with_user_details_dtos = []
        for stage_details_dto in stage_details_dtos:
            stage_id_with_name_dto = StageIdWithNameDTO(
                db_stage_id=stage_details_dto.db_stage_id,
                stage_display_name=stage_details_dto.name)
            stage_with_user_details_dtos.append(
                StageWithUserDetailsDTO(
                    stage_details_dto=stage_id_with_name_dto,
                    assignee_details_dto=user_details_dto))
        return stage_with_user_details_dtos

    def _get_stage_with_user_details_and_team_details_dto(
            self, stages_with_user_details_dtos: List[StageWithUserDetailsDTO],
            project_id: str) -> StageWithUserDetailsAndTeamDetailsDTO:
        assignee_ids = self._get_assignees_of_stages_having_user_details_dtos(
            stages_with_user_details_dtos)
        user_id_with_team_details_dtos = self. \
            _get_team_details_of_given_assignee_ids_based_on_project(
            assignee_ids=assignee_ids, project_id=project_id)

        stage_with_user_details_and_team_details_dto = \
            StageWithUserDetailsAndTeamDetailsDTO(
                stages_with_user_details_dtos=
                stages_with_user_details_dtos,
                user_with_team_details_dtos=user_id_with_team_details_dtos)
        return stage_with_user_details_and_team_details_dto

    @staticmethod
    def _get_team_details_of_given_assignee_ids_based_on_project(
            assignee_ids: List[str], project_id: str) -> List[
        UserIdWIthTeamDetailsDTO]:
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        user_id_with_team_details_dtos = auth_service_adapter. \
            get_team_info_for_given_user_ids(user_ids=assignee_ids,
                                             project_id=project_id)
        user_with_first_team_details_dtos = []
        for user_id_with_team_details_dto in user_id_with_team_details_dtos:
            from ib_tasks.adapters.dtos import UserIdWIthTeamDetailsDTO
            user_with_first_team_details_dtos.append(UserIdWIthTeamDetailsDTO(
                user_id=user_id_with_team_details_dto.user_id, team_details=
                user_id_with_team_details_dto.team_details[0]))
        return user_with_first_team_details_dtos

    @staticmethod
    def _get_assignees_of_stages_having_user_details_dtos(
            stages_having_user_details_dtos: List[StageWithUserDetailsDTO]) \
            -> List[str]:
        assignee_ids = []
        for stages_having_user_details_dto in stages_having_user_details_dtos:
            if stages_having_user_details_dto.assignee_details_dto is None:
                continue
            assignee_id = stages_having_user_details_dto.assignee_details_dto. \
                assignee_id
            assignee_ids.append(assignee_id)
        assignee_ids = list(set(assignee_ids))
        return assignee_ids

    def _get_role_ids_group_by_stage_id_dtos_given_stages(
            self, db_stage_ids: List[int]) -> List[StageIdWithRoleIdsDTO]:
        stage_role_dtos = self.stage_storage. \
            get_stage_role_dtos_given_db_stage_ids(db_stage_ids=db_stage_ids)
        role_ids_group_by_stage_id_dtos = \
            self._get_role_ids_group_by_stage_id_dtos_given_stages_and_roles(
                stage_ids=db_stage_ids, stage_role_dtos=stage_role_dtos)
        return role_ids_group_by_stage_id_dtos

    def _get_previous_user_or_user_having_less_tasks_details_dtos_for_given_stages(
            self, db_stage_ids: List[int], stage_detail_dtos:
            List[StageDetailsDTO], project_id: str, task_id: int) -> \
            List[StageWithUserDetailsDTO]:
        role_ids_group_by_stage_id_dtos = self. \
            _get_role_ids_group_by_stage_id_dtos_given_stages(
            db_stage_ids=db_stage_ids)
        stage_with_user_details_dtos = []
        if len(db_stage_ids) == 1:
            previous_stage_ids = self.stage_storage.get_recent_task_stage(
                task_id=task_id)
            if len(previous_stage_ids) == 1:
                stage_with_user_details_dtos = self. \
                    _get_previous_user_details_for_next_stage_if_user_is_permitted(
                    task_id=task_id,
                    previous_stage_ids=previous_stage_ids,
                    next_task_stage_ids=db_stage_ids, project_id=project_id,
                    stage_detail_dtos=stage_detail_dtos)
        if stage_with_user_details_dtos == [] or len(db_stage_ids) != 1:
            stage_with_user_details_dtos = self. \
                _get_user_details_dtos_having_less_tasks_for_given_stages_and_roles(
                role_ids_group_by_stage_id_dtos=role_ids_group_by_stage_id_dtos,
                stage_detail_dtos=stage_detail_dtos, project_id=project_id)
        return stage_with_user_details_dtos

    def _get_previous_user_details_for_next_stage_if_user_is_permitted(
            self, task_id: int, previous_stage_ids: List[int],
            next_task_stage_ids: List[int], project_id: str,
            stage_detail_dtos: List[StageDetailsDTO]) -> List[
        StageWithUserDetailsDTO]:
        task_stage_assignee_dto = self.stage_storage. \
            get_stage_details_having_assignees_in_given_stage_ids(
            task_id=task_id, db_stage_ids=previous_stage_ids)
        role_ids_group_by_stage_id_dtos = self. \
            _get_role_ids_group_by_stage_id_dtos_given_stages(
            db_stage_ids=next_task_stage_ids)
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        permitted_user_details_dtos = auth_service_adapter. \
            get_permitted_user_details(
            role_ids=role_ids_group_by_stage_id_dtos[0].role_ids,
            project_id=project_id)
        permitted_user_ids = [each_user_details_dto.user_id
                              for each_user_details_dto in
                              permitted_user_details_dtos]
        if task_stage_assignee_dto[0].assignee_id in permitted_user_ids:
            user_details_dto = \
                self._get_user_details_dto_of_given_user(
                    user_details_dtos=permitted_user_details_dtos,
                    user_id=task_stage_assignee_dto[0].assignee_id)
            stage_with_user_details_dto = self. \
                _prepare_stage_with_user_details_dto(
                stage_detail_dtos=stage_detail_dtos,
                role_ids_group_by_stage_id_dto=
                role_ids_group_by_stage_id_dtos[0],
                permitted_user_details_dto_having_less_tasks=
                user_details_dto)
            previous_user_details_dto_with_stage_for_next_stage = [
                stage_with_user_details_dto]
            return previous_user_details_dto_with_stage_for_next_stage
        return []

    def _get_assignee_with_current_tasks_count_dtos(self) \
            -> List[AssigneeCurrentTasksCountDTO]:
        task_stage_dtos_of_tasks_that_are_not_yet_completed = self. \
            _get_task_stage_dtos_of_tasks_that_are_not_yet_completed()
        stage_ids_of_tasks_that_are_not_yet_completed = list(
            set([each_task_stage_dto.db_stage_id for each_task_stage_dto in
                 task_stage_dtos_of_tasks_that_are_not_yet_completed]))
        task_ids_of_tasks_that_are_not_yet_completed = list(set([
            each_task_stage_dto.task_id for each_task_stage_dto in
            task_stage_dtos_of_tasks_that_are_not_yet_completed]))
        assignee_with_current_tasks_count_dtos = self.task_stage_storage. \
            get_current_count_of_tasks_assigned_for_each_user(
            db_stage_ids=stage_ids_of_tasks_that_are_not_yet_completed,
            task_ids=task_ids_of_tasks_that_are_not_yet_completed)
        return assignee_with_current_tasks_count_dtos

    @staticmethod
    def _prepare_permitted_user_dtos_not_in_current_tasks_with_zero_tasks_count(
            permitted_user_ids: List[str], assignee_ids_with_current_task_count
            : List[str]) -> List[AssigneeCurrentTasksCountDTO]:
        permitted_user_dtos_not_in_current_tasks = [
            AssigneeCurrentTasksCountDTO(assignee_id=permitted_user_id,
                                         tasks_count=0)
            for permitted_user_id in permitted_user_ids
            if permitted_user_id not in assignee_ids_with_current_task_count]
        return permitted_user_dtos_not_in_current_tasks

    @staticmethod
    def _get_assignee_ids_having_current_task_count(
            assignee_with_current_tasks_count_dtos:
            List[AssigneeCurrentTasksCountDTO]) -> List[str]:
        assignee_ids_with_current_task_count = []
        if assignee_with_current_tasks_count_dtos:
            assignee_ids_with_current_task_count = [
                assignee_dto.assignee_id for
                assignee_dto in assignee_with_current_tasks_count_dtos]
        return assignee_ids_with_current_task_count

    def _get_permitted_assignee_with_current_tasks_count_dtos(
            self, permitted_user_details_dtos: List[UserDetailsDTO],
            assignee_with_current_tasks_count_dtos:
            List[AssigneeCurrentTasksCountDTO],
            updated_task_count_dtos_for_assignee_having_less_tasks:
            List[AssigneeCurrentTasksCountDTO]) \
            -> List[AssigneeCurrentTasksCountDTO]:
        assignee_ids_with_current_task_count = \
            self._get_assignee_ids_having_current_task_count(
                assignee_with_current_tasks_count_dtos)
        permitted_user_dtos_not_in_current_tasks_with_zero_tasks_count, \
        permitted_user_ids = [], []
        if permitted_user_details_dtos:
            permitted_user_ids = [each_user_details_dto.user_id
                                  for each_user_details_dto in
                                  permitted_user_details_dtos]
            permitted_user_dtos_not_in_current_tasks_with_zero_tasks_count = \
                self._prepare_permitted_user_dtos_not_in_current_tasks_with_zero_tasks_count(
                    permitted_user_ids, assignee_ids_with_current_task_count)
        assignee_with_all_current_tasks_count_dtos = \
            assignee_with_current_tasks_count_dtos + \
            permitted_user_dtos_not_in_current_tasks_with_zero_tasks_count
        permitted_assignee_with_current_tasks_count_dtos = \
            [assignee_dto for assignee_dto in
             assignee_with_all_current_tasks_count_dtos
             if assignee_dto.assignee_id in permitted_user_ids]
        permitted_assignee_with_updated_tasks_count_dtos = \
            self._get_permitted_assignee_with_db_current_tasks_count_along_with_updated_tasks_count_dtos(
                permitted_assignee_with_current_tasks_count_dtos=
                permitted_assignee_with_current_tasks_count_dtos,
                updated_task_count_dtos_for_assignee_having_less_tasks=
                updated_task_count_dtos_for_assignee_having_less_tasks)
        return permitted_assignee_with_updated_tasks_count_dtos

    @staticmethod
    def _get_permitted_assignee_with_db_current_tasks_count_along_with_updated_tasks_count_dtos(
            permitted_assignee_with_current_tasks_count_dtos:
            List[AssigneeCurrentTasksCountDTO],
            updated_task_count_dtos_for_assignee_having_less_tasks:
            List[AssigneeCurrentTasksCountDTO]) -> \
            List[AssigneeCurrentTasksCountDTO]:
        for permitted_assignee_dto in permitted_assignee_with_current_tasks_count_dtos:
            for updated_task_count_dto_of_assignee in \
                    updated_task_count_dtos_for_assignee_having_less_tasks:
                if permitted_assignee_dto.assignee_id \
                        == updated_task_count_dto_of_assignee.assignee_id:
                    permitted_assignee_dto.tasks_count \
                        = updated_task_count_dto_of_assignee.tasks_count
        return permitted_assignee_with_current_tasks_count_dtos

    @staticmethod
    def any_in(user_roles: List[str], stage_roles: List[str]) -> bool:
        from ib_iam.constants.config import ALL_ROLES_ID
        return any(role in stage_roles for role in
                   user_roles) or ALL_ROLES_ID in stage_roles

    def _get_user_details_dtos_having_less_tasks_for_given_stages_and_roles(
            self, role_ids_group_by_stage_id_dtos: List[StageIdWithRoleIdsDTO],
            stage_detail_dtos: List[StageDetailsDTO], project_id: str) -> \
            List[StageWithUserDetailsDTO]:
        assignee_with_current_tasks_count_dtos = self. \
            _get_assignee_with_current_tasks_count_dtos()
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        stage_with_user_details_dtos_having_less_tasks, \
        updated_task_count_dtos_for_assignee_having_less_tasks = [], []
        role_ids = []
        for role_ids_group_by_stage_id_dto in role_ids_group_by_stage_id_dtos:
            role_ids += role_ids_group_by_stage_id_dto.role_ids
        role_ids = sorted(list(set(role_ids)))
        permitted_user_details_dtos = \
            auth_service_adapter.get_user_details_with_roles(role_ids,
                                                             project_id)
        from collections import defaultdict
        stage_with_permitted_user_dict = defaultdict(list)
        for role_ids_group_by_stage_id_dto in role_ids_group_by_stage_id_dtos:
            stage_id = role_ids_group_by_stage_id_dto.db_stage_id
            stage_roles = role_ids_group_by_stage_id_dto.role_ids
            for user_details_dto in permitted_user_details_dtos:
                user_is_stage_permitted = (
                    self.any_in(user_details_dto.roles, stage_roles))
                if user_is_stage_permitted:
                    stage_with_permitted_user_dict[stage_id].append(
                        user_details_dto)
        for each_dto in role_ids_group_by_stage_id_dtos:
            permitted_user_details_dtos = stage_with_permitted_user_dict[
                each_dto.db_stage_id]
            permitted_assignee_with_current_tasks_count_dtos = self. \
                _get_permitted_assignee_with_current_tasks_count_dtos(
                permitted_user_details_dtos,
                assignee_with_current_tasks_count_dtos,
                updated_task_count_dtos_for_assignee_having_less_tasks)
            permitted_user_details_dto_having_less_tasks = self. \
                _get_permitted_user_details_dto_having_less_tasks(
                permitted_assignee_with_current_tasks_count_dtos,
                permitted_user_details_dtos,
                updated_task_count_dtos_for_assignee_having_less_tasks)
            stage_with_user_details_dto_having_less_tasks = self. \
                _prepare_stage_with_user_details_dto(
                stage_detail_dtos=stage_detail_dtos,
                role_ids_group_by_stage_id_dto=each_dto,
                permitted_user_details_dto_having_less_tasks=
                permitted_user_details_dto_having_less_tasks)
            stage_with_user_details_dtos_having_less_tasks.append(
                stage_with_user_details_dto_having_less_tasks)
        return stage_with_user_details_dtos_having_less_tasks

    def _get_permitted_user_details_dto_having_less_tasks(
            self, permitted_assignee_with_current_tasks_count_dtos: List[
                AssigneeCurrentTasksCountDTO],
            permitted_user_details_dtos: List[UserDetailsDTO],
            updated_task_count_dtos_for_assignee_having_less_tasks: List[
                AssigneeCurrentTasksCountDTO]) -> Union[list, UserDetailsDTO]:
        empty_permitted_assignee_with_current_tasks_count_dtos = \
            permitted_assignee_with_current_tasks_count_dtos == []
        permitted_user_details_dto_having_less_tasks = []
        if empty_permitted_assignee_with_current_tasks_count_dtos:
            return permitted_user_details_dto_having_less_tasks

        assignee_id_with_current_less_tasks, \
        updated_task_count_dtos_for_assignee_having_less_tasks = \
            self._get_permitted_user_having_less_tasks_for_each_stage(
                permitted_assignee_with_current_tasks_count_dtos,
                updated_task_count_dtos_for_assignee_having_less_tasks)
        permitted_user_details_dto_having_less_tasks = \
            self._get_user_details_dto_of_given_user(
                user_details_dtos=permitted_user_details_dtos,
                user_id=assignee_id_with_current_less_tasks)

        return permitted_user_details_dto_having_less_tasks

    def _get_user_details_dto_of_given_user(self, user_details_dtos: List[
        UserDetailsDTO], user_id: str) -> Optional[UserDetailsDTO]:
        user_details_dto = None
        for user_details_dto in user_details_dtos:
            if user_id == user_details_dto.user_id:
                user_details_dto = user_details_dto
                break
        return user_details_dto

    def _get_permitted_user_having_less_tasks_for_each_stage(
            self, permitted_assignee_with_current_tasks_count_dtos:
            List[AssigneeCurrentTasksCountDTO],
            updated_task_count_dtos_for_assignee_having_less_tasks:
            List[AssigneeCurrentTasksCountDTO]) -> \
            Tuple[str, List[AssigneeCurrentTasksCountDTO]]:
        permitted_assignee_with_current_tasks_count_dtos_dict = \
            sorted([assignee_with_current_tasks_count_dto.__dict__
                    for assignee_with_current_tasks_count_dto in
                    permitted_assignee_with_current_tasks_count_dtos],
                   key=lambda i: i['tasks_count'])

        updated_task_count_dto_for_assignee_having_less_tasks_dict = \
            [updated_task_count_dto_for_assignee.__dict__
             for updated_task_count_dto_for_assignee in
             updated_task_count_dtos_for_assignee_having_less_tasks]
        assignee_id_with_current_less_tasks = \
            permitted_assignee_with_current_tasks_count_dtos_dict[0][
                'assignee_id']
        assignee_id_index = self._get_assignee_id_index_given_assignee_id(
            updated_task_count_dto_for_assignee_having_less_tasks_dict,
            assignee_id_with_current_less_tasks)
        if assignee_id_index is None:
            task_count_dto_of_assignee_not_in_updated_task_count_dtos = \
                self._get_updated_task_count_dto_of_assignee(
                    assignee_id=assignee_id_with_current_less_tasks,
                    tasks_count=
                    permitted_assignee_with_current_tasks_count_dtos_dict[0][
                        'tasks_count'])
            updated_task_count_dtos_for_assignee_having_less_tasks.append(
                task_count_dto_of_assignee_not_in_updated_task_count_dtos)
            return assignee_id_with_current_less_tasks, \
                   updated_task_count_dtos_for_assignee_having_less_tasks

        updated_task_count_dto_for_assignee_having_less_tasks_dict[
            assignee_id_index]['tasks_count'] += 1

        updated_task_count_dtos_for_assignee_having_less_tasks = \
            [AssigneeCurrentTasksCountDTO(
                assignee_id=updated_task_count_dict_for_assignee
                ['assignee_id'],
                tasks_count=updated_task_count_dict_for_assignee[
                    'tasks_count']) for updated_task_count_dict_for_assignee in
                updated_task_count_dto_for_assignee_having_less_tasks_dict]

        return assignee_id_with_current_less_tasks, \
               updated_task_count_dtos_for_assignee_having_less_tasks

    @staticmethod
    def _get_updated_task_count_dto_of_assignee(
            assignee_id: str, tasks_count: int):
        updated_task_count_dto_of_assignee = AssigneeCurrentTasksCountDTO(
            assignee_id=assignee_id,
            tasks_count=tasks_count + 1)
        return updated_task_count_dto_of_assignee

    def _get_updated_task_count_dtos_for_assignee_having_less_tasks(
            self, permitted_assignee_with_current_tasks_count_dtos,
            assignee_id_with_current_less_tasks,
            updated_task_count_dtos_for_assignee_having_less_tasks):
        for assignee_with_tasks_count_dto in \
                permitted_assignee_with_current_tasks_count_dtos:
            if assignee_with_tasks_count_dto.assignee_id == \
                    assignee_id_with_current_less_tasks:
                task_count_dto_of_assignee = self. \
                    _get_updated_task_count_dto_of_assignee(
                    assignee_id_with_current_less_tasks,
                    assignee_with_tasks_count_dto.tasks_count)
                updated_task_count_dtos_for_assignee_having_less_tasks. \
                    append(task_count_dto_of_assignee)
            return updated_task_count_dtos_for_assignee_having_less_tasks

    @staticmethod
    def _get_assignee_id_index_given_assignee_id(
            updated_task_count_dto_for_assignee_having_less_tasks_dict,
            assignee_id: str) -> int:
        assignee_id_index = next(
            (index for (index, d) in enumerate(
                updated_task_count_dto_for_assignee_having_less_tasks_dict)
             if d["assignee_id"] == assignee_id), None)
        # #FIXME: Handle assignee id index none usecase
        # if assignee_id_index is None:
        #     assignee_id_index = 0
        return assignee_id_index

    def _get_task_stage_dtos_of_tasks_that_are_not_yet_completed(
            self) -> List[TaskWithDbStageIdDTO]:
        all_tasks_with_current_stage_id_dtos = self. \
            stage_storage.get_current_stages_of_all_tasks()
        current_stage_ids_of_tasks = list(
            set([task_with_stage_id_dto.db_stage_id
                 for task_with_stage_id_dto in
                 all_tasks_with_current_stage_id_dtos]))
        current_stage_ids_having_actions = \
            self.action_storage.get_stage_ids_having_actions(
                db_stage_ids=current_stage_ids_of_tasks)
        task_stage_dtos_of_tasks_that_are_not_yet_completed = [
            each_task_with_stage_id_dto for each_task_with_stage_id_dto in
            all_tasks_with_current_stage_id_dtos
            if each_task_with_stage_id_dto.db_stage_id in \
               current_stage_ids_having_actions]
        return task_stage_dtos_of_tasks_that_are_not_yet_completed

    def _prepare_stage_with_user_details_dto(
            self, stage_detail_dtos: List[StageDetailsDTO],
            role_ids_group_by_stage_id_dto: StageIdWithRoleIdsDTO,
            permitted_user_details_dto_having_less_tasks: UserDetailsDTO) -> \
            StageWithUserDetailsDTO:
        stage_display_name = self. \
            _get_matched_stage_display_name_for_given_stage_id(
            stage_detail_dtos,
            db_stage_id=role_ids_group_by_stage_id_dto.db_stage_id)
        assignee_details_dto = None
        if permitted_user_details_dto_having_less_tasks:
            assignee_details_dto = AssigneeDetailsDTO(
                assignee_id=
                permitted_user_details_dto_having_less_tasks.user_id,
                name=permitted_user_details_dto_having_less_tasks.user_name,
                profile_pic_url=permitted_user_details_dto_having_less_tasks.
                    profile_pic_url)
        stage_detail_dto = StageIdWithNameDTO(
            db_stage_id=role_ids_group_by_stage_id_dto.db_stage_id,
            stage_display_name=stage_display_name)
        stage_with_user_details_dto = StageWithUserDetailsDTO(
            stage_details_dto=stage_detail_dto,
            assignee_details_dto=assignee_details_dto)
        return stage_with_user_details_dto

    @staticmethod
    def _get_matched_stage_display_name_for_given_stage_id(
            stage_detail_dtos: List[StageDetailsDTO], db_stage_id: int) -> str:
        name = None
        for each_stage_detail_dto in stage_detail_dtos:
            if each_stage_detail_dto.db_stage_id == db_stage_id:
                name = each_stage_detail_dto.name
        return name

    @staticmethod
    def _get_role_ids_group_by_stage_id_dtos_given_stages_and_roles(
            stage_ids: List[int], stage_role_dtos: List[StageRoleDTO]) \
            -> List[StageIdWithRoleIdsDTO]:
        role_ids_group_by_stage_id_dtos = []
        for each_stage_id in stage_ids:
            role_ids = [each_stage_role_dto.role_id
                        for each_stage_role_dto in stage_role_dtos
                        if each_stage_role_dto.db_stage_id == each_stage_id]
            each_stage_id_with_role_ids_dto = \
                StageIdWithRoleIdsDTO(db_stage_id=each_stage_id,
                                      role_ids=role_ids)
            role_ids_group_by_stage_id_dtos.append(
                each_stage_id_with_role_ids_dto)
        return role_ids_group_by_stage_id_dtos

    @staticmethod
    def _get_db_stage_ids_given_stage_detail_dtos(
            stage_detail_dtos: List[StageDetailsDTO]) -> List[int]:
        db_stage_ids = [each_stage_detail_dto.db_stage_id
                        for each_stage_detail_dto in stage_detail_dtos]
        return db_stage_ids
