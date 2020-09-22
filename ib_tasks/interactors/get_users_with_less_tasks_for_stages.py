from typing import List, Tuple, Union
from ib_tasks.adapters.dtos import UserDetailsDTO, AssigneeDetailsDTO
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
from ib_tasks.adapters.dtos import UserIdWIthTeamDetailsDTO


class GetUsersWithLessTasksInGivenStagesInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.stage_storage = stage_storage
        self.action_storage = action_storage
        self.task_stage_storage = task_stage_storage

    def get_users_with_less_tasks_in_given_stages(
            self, stage_ids: List[str],
            project_id: str) -> StageWithUserDetailsAndTeamDetailsDTO:

        stage_detail_dtos = self.stage_storage. \
            get_stage_detail_dtos_given_stage_ids(stage_ids=stage_ids)
        db_stage_ids = self._get_db_stage_ids_given_stage_detail_dtos(
            stage_detail_dtos)

        user_details_dtos_having_less_tasks_for_given_stages = self. \
            _get_user_details_dtos_having_less_tasks_for_given_stages(
            db_stage_ids=db_stage_ids, stage_detail_dtos=stage_detail_dtos,
            project_id=project_id)

        assignee_ids = self._get_assignees_of_stages_having_user_details_dtos(
            user_details_dtos_having_less_tasks_for_given_stages)
        user_id_with_team_details_dtos = self. \
            _get_team_details_of_given_assignee_ids_based_on_project(
            assignee_ids=assignee_ids, project_id=project_id)

        stage_with_user_details_and_team_details_dto = \
            StageWithUserDetailsAndTeamDetailsDTO(
                stages_with_user_details_dtos=
                user_details_dtos_having_less_tasks_for_given_stages,
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
            stages_having_user_details_dtos: List[StageWithUserDetailsDTO])\
            -> List[str]:
        assignee_ids = []
        for stages_having_user_details_dto in stages_having_user_details_dtos:
            if stages_having_user_details_dto.assignee_details_dto is None:
                continue
            assignee_id = stages_having_user_details_dto.assignee_details_dto.\
                    assignee_id
            assignee_ids.append(assignee_id)
        assignee_ids = list(set(assignee_ids))
        return assignee_ids

    def _get_user_details_dtos_having_less_tasks_for_given_stages(
            self, db_stage_ids: List[int], stage_detail_dtos:
            List[StageDetailsDTO], project_id: str) -> \
            List[StageWithUserDetailsDTO]:
        stage_role_dtos = self.stage_storage. \
            get_stage_role_dtos_given_db_stage_ids(db_stage_ids=db_stage_ids)
        role_ids_group_by_stage_id_dtos = \
            self._get_role_ids_group_by_stage_id_dtos(
                stage_ids=db_stage_ids, stage_role_dtos=stage_role_dtos)
        stage_with_user_details_dtos_having_less_tasks = self. \
            _get_user_details_dtos_having_less_tasks_for_given_stages_and_roles(
            role_ids_group_by_stage_id_dtos=role_ids_group_by_stage_id_dtos,
            stage_detail_dtos=stage_detail_dtos, project_id=project_id)
        return stage_with_user_details_dtos_having_less_tasks

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

    def _get_user_details_dtos_having_less_tasks_for_given_stages_and_roles(
            self, role_ids_group_by_stage_id_dtos: List[StageIdWithRoleIdsDTO],
            stage_detail_dtos: List[StageDetailsDTO], project_id: str) -> \
            List[StageWithUserDetailsDTO]:
        assignee_with_current_tasks_count_dtos = self. \
            _get_assignee_with_current_tasks_count_dtos()
        from ib_tasks.adapters.auth_service import AuthService
        auth_service_adapter = AuthService()
        stage_with_user_details_dtos, \
        updated_task_count_dtos_for_assignee_having_less_tasks = [], []
        for each_dto in role_ids_group_by_stage_id_dtos:
            permitted_user_details_dtos = auth_service_adapter. \
                get_permitted_user_details(role_ids=each_dto.role_ids,
                                           project_id=project_id)
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
            stage_with_user_details_dto = self. \
                _prepare_stage_with_user_details_dto(
                stage_detail_dtos=stage_detail_dtos,
                role_ids_group_by_stage_id_dto=each_dto,
                permitted_user_details_dto_having_less_tasks=
                permitted_user_details_dto_having_less_tasks)
            stage_with_user_details_dtos.append(stage_with_user_details_dto)
        return stage_with_user_details_dtos

    def _get_permitted_user_details_dto_having_less_tasks(
            self, permitted_assignee_with_current_tasks_count_dtos: List[
                AssigneeCurrentTasksCountDTO],
            permitted_user_details_dtos: List[UserDetailsDTO],
            updated_task_count_dtos_for_assignee_having_less_tasks: List[
                AssigneeCurrentTasksCountDTO]) -> Union[list, UserDetailsDTO]:
        empty_permitted_assignee_with_current_tasks_count_dtos = \
            permitted_assignee_with_current_tasks_count_dtos == []
        if empty_permitted_assignee_with_current_tasks_count_dtos:
            permitted_user_details_dto_having_less_tasks = []
            return permitted_user_details_dto_having_less_tasks

        assignee_id_with_current_less_tasks, \
        updated_task_count_dtos_for_assignee_having_less_tasks = \
            self._get_permitted_user_having_less_tasks_for_each_stage(
                permitted_assignee_with_current_tasks_count_dtos,
                updated_task_count_dtos_for_assignee_having_less_tasks)
        for permitted_user_details_dto in permitted_user_details_dtos:
            if assignee_id_with_current_less_tasks == \
                    permitted_user_details_dto.user_id:
                permitted_user_details_dto_having_less_tasks = \
                    permitted_user_details_dto
                break
        return permitted_user_details_dto_having_less_tasks

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
    def _get_role_ids_group_by_stage_id_dtos(
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
