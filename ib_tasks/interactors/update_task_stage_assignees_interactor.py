from typing import List

from ib_tasks.exceptions.permission_custom_exceptions import \
    InvalidUserIdException
from ib_tasks.exceptions.stage_custom_exceptions import \
    DuplicateStageIds, \
    StageIdsWithInvalidPermissionForAssignee, InvalidDbStageIdsListException, \
    VirtualStageIdsException
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTaskIdException, \
    InvalidTaskDisplayId
from ib_tasks.interactors.mixins.get_task_id_for_task_display_id_mixin import \
    GetTaskIdForTaskDisplayIdMixin
from ib_tasks.interactors.presenter_interfaces \
    .update_task_stage_assignees_presenter_interface import \
    UpdateTaskStageAssigneesPresenterInterface
from ib_tasks.interactors.stages_dtos import TaskIdWithStageAssigneesDTO, \
    TaskIdWithStageAssigneeDTO, TaskDisplayIdWithStageAssigneesDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO, \
    StageIdWithRoleIdsAndAssigneeIdDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class UpdateTaskStageAssigneesInteractor(GetTaskIdForTaskDisplayIdMixin):
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def update_task_stage_assignees_wrapper(
            self, task_display_id_with_stage_assignees_dto:
            TaskDisplayIdWithStageAssigneesDTO,
            presenter: UpdateTaskStageAssigneesPresenterInterface):

        try:
            task_id = self.get_task_id_for_task_display_id(
                task_display_id_with_stage_assignees_dto.task_display_id)
            task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
                task_id=task_id,
                stage_assignees=task_display_id_with_stage_assignees_dto.
                    stage_assignees)
            self.validate_and_update_task_stage_assignees(
                task_id_with_stage_assignees_dto)
        except InvalidTaskDisplayId as err:
            return presenter.raise_invalid_task_display_id(err)
        except DuplicateStageIds as exception:
            return presenter.raise_duplicate_stage_ids_not_valid(
                duplicate_stage_ids=exception.duplicate_stage_ids)
        except InvalidDbStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except VirtualStageIdsException as exception:
            return presenter.raise_virtual_stage_ids_exception(
                virtual_stage_ids=exception.virtual_stage_ids)
        except InvalidUserIdException as exception:
            return presenter.raise_invalid_user_id_exception(user_id=
                                                             exception.user_id)

        except StageIdsWithInvalidPermissionForAssignee as exception:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                invalid_stage_ids=exception.invalid_stage_ids)

    def validate_and_update_task_stage_assignees(
            self,
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO):
        self.validations_of_request(task_id_with_stage_assignees_dto)
        self.update_task_stage_assignees(task_id_with_stage_assignees_dto)

    def validations_of_request(self,
                               task_id_with_stage_assignees_dto:
                               TaskIdWithStageAssigneesDTO):
        stage_ids = self._get_stage_ids_from_given_dto(
            task_id_with_stage_assignees_dto)
        self._check_duplicate_stage_ids(stage_ids)
        stage_dtos = self.stage_storage. \
            get_valid_db_stage_ids_with_stage_value(stage_ids)
        virtual_stage_ids = [stage_dto.db_stage_id for stage_dto in stage_dtos
                             if stage_dto.stage_value == -1]

        valid_stage_ids = [stage_dto.db_stage_id for stage_dto in stage_dtos if
                           stage_dto.db_stage_id not in virtual_stage_ids]
        stage_ids_in_db = valid_stage_ids + virtual_stage_ids
        self._validate_stage_ids(stage_ids, stage_ids_in_db)
        if virtual_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                VirtualStageIdsException
            raise VirtualStageIdsException(virtual_stage_ids)
        stage_role_dtos = self.stage_storage. \
            get_stage_role_dtos_given_db_stage_ids(stage_ids)

        role_ids_and_assignee_id_group_by_stage_id_dtos = \
            self._get_role_ids_and_assignee_id_group_by_stage_id_dtos(
                stage_ids=stage_ids, stage_role_dtos=stage_role_dtos,
                task_id_with_stage_assignees_dto=
                task_id_with_stage_assignees_dto
            )
        self._validate_does_given_assignee_of_stage_ids_have_valid_permission(
            role_ids_and_assignee_id_group_by_stage_id_dtos)
        return

    def update_task_stage_assignees(
            self,
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO):

        task_id = task_id_with_stage_assignees_dto.task_id
        stage_ids = self._get_stage_ids_from_given_dto(
            task_id_with_stage_assignees_dto)
        stage_assignee_dtos_having_assignees = self.stage_storage. \
            get_task_stages_assignees_without_having_left_at_status(
            task_id=task_id, db_stage_ids=stage_ids)
        matched_stage_assignee_dtos = []
        user_given_stage_assignee_dtos = task_id_with_stage_assignees_dto. \
            stage_assignees
        for user_given_stage_assignee_dto in user_given_stage_assignee_dtos:
            for stage_assignee_dto_having_assignees in \
                    stage_assignee_dtos_having_assignees:
                if user_given_stage_assignee_dto == \
                        stage_assignee_dto_having_assignees:
                    matched_stage_assignee_dtos.append(
                        stage_assignee_dto_having_assignees)
        matched_stage_ids_in_stage_assignee_dtos = [
            matched_stage_assignee_dto.db_stage_id for
            matched_stage_assignee_dto in matched_stage_assignee_dtos]
        stage_ids_that_are_not_matched = [stage_id for stage_id in stage_ids
                                          if stage_id not in
                                          matched_stage_ids_in_stage_assignee_dtos]
        current_task_stage_ids = self.stage_storage. \
            get_current_stage_db_ids_of_task(
            task_id=task_id)
        current_task_stage_ids_that_are_not_in_given_stage_ids = list(
            set(current_task_stage_ids) - set(stage_ids))
        matched_stage_ids_in_stage_assignee_dtos = \
            matched_stage_ids_in_stage_assignee_dtos + \
            current_task_stage_ids_that_are_not_in_given_stage_ids

        self.stage_storage. \
            update_task_stages_other_than_matched_stages_with_left_at_status(
            task_id=task_id,
            db_stage_ids=matched_stage_ids_in_stage_assignee_dtos)

        task_id_with_stage_assignee_dtos_for_creation = self. \
            _get_task_id_with_stage_assignee_dtos_given_task_stage_ids(
            stage_ids_that_are_not_matched, task_id_with_stage_assignees_dto)
        self.stage_storage.create_task_stage_assignees(
            task_id_with_stage_assignee_dtos=
            task_id_with_stage_assignee_dtos_for_creation)
        return

    @staticmethod
    def _get_task_id_with_stage_assignee_dtos_given_task_stage_ids(
            task_stage_ids,
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO
    ) -> List[TaskIdWithStageAssigneeDTO]:
        task_id = task_id_with_stage_assignees_dto.task_id
        task_id_with_stage_assignee_dtos = []
        for each_task_stage_id in task_stage_ids:
            for each_task_id_with_stage_assignees_dto in \
                    task_id_with_stage_assignees_dto.stage_assignees:
                if each_task_id_with_stage_assignees_dto.db_stage_id == \
                        each_task_stage_id:
                    task_id_with_stage_assignee_dtos.append(
                        TaskIdWithStageAssigneeDTO(
                            assignee_id=each_task_id_with_stage_assignees_dto.
                                assignee_id,
                            db_stage_id=each_task_stage_id,
                            task_id=task_id,
                            team_id=each_task_id_with_stage_assignees_dto.team_id))

        return task_id_with_stage_assignee_dtos

    @staticmethod
    def _validate_does_given_assignee_of_stage_ids_have_valid_permission(
            role_ids_and_assignee_id_group_by_stage_id_dtos: List[
                StageIdWithRoleIdsAndAssigneeIdDTO]):
        stage_ids_with_invalid_permission_for_assignee_id = []
        user_role_validation_interactor = UserRoleValidationInteractor()
        for each_stage_id_with_role_ids_and_assignee_id_dto in \
                role_ids_and_assignee_id_group_by_stage_id_dtos:
            user_has_required_permission = True
            if each_stage_id_with_role_ids_and_assignee_id_dto.assignee_id is not None:
                user_has_required_permission = user_role_validation_interactor. \
                    does_user_has_required_permission(
                    user_id=each_stage_id_with_role_ids_and_assignee_id_dto.
                        assignee_id,
                    role_ids=each_stage_id_with_role_ids_and_assignee_id_dto.
                        role_ids)
            user_doesnt_has_required_permission = not \
                user_has_required_permission
            if user_doesnt_has_required_permission:
                stage_ids_with_invalid_permission_for_assignee_id. \
                    append(each_stage_id_with_role_ids_and_assignee_id_dto.
                           db_stage_id)
        if stage_ids_with_invalid_permission_for_assignee_id:
            raise StageIdsWithInvalidPermissionForAssignee(
                stage_ids_with_invalid_permission_for_assignee_id)
        return

    @staticmethod
    def _get_role_ids_and_assignee_id_group_by_stage_id_dtos(
            stage_ids: List[int],
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO,
            stage_role_dtos: List[StageRoleDTO]
    ) -> List[StageIdWithRoleIdsAndAssigneeIdDTO]:
        role_ids_and_assignee_id_group_by_stage_id_dtos = []
        for each_stage_id in stage_ids:
            list_of_role_ids = []
            for each_stage_role_dto in \
                    stage_role_dtos:
                if each_stage_role_dto.db_stage_id == \
                        each_stage_id:
                    list_of_role_ids.append(each_stage_role_dto.role_id)
            stage_assignee_id = None
            for each_stage_assignee_dto in task_id_with_stage_assignees_dto. \
                    stage_assignees:
                if each_stage_assignee_dto.db_stage_id == each_stage_id:
                    stage_assignee_id = each_stage_assignee_dto.assignee_id

            each_stage_id_with_role_ids_and_assignee_id_dto = \
                StageIdWithRoleIdsAndAssigneeIdDTO(
                    db_stage_id=each_stage_id,
                    role_ids=list_of_role_ids,
                    assignee_id=stage_assignee_id)
            role_ids_and_assignee_id_group_by_stage_id_dtos.append(
                each_stage_id_with_role_ids_and_assignee_id_dto)
        return role_ids_and_assignee_id_group_by_stage_id_dtos

    def _validate_task_id(self, task_id: int):
        is_task_exists = self.task_storage. \
            check_is_task_exists(
            task_id=task_id)

        is_task_does_not_exists = not is_task_exists
        if is_task_does_not_exists:
            raise InvalidTaskIdException(task_id=task_id)

    @staticmethod
    def _get_stage_ids_from_given_dto(
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO):
        stage_ids = [
            stage_assignee_dto.db_stage_id for stage_assignee_dto in
            task_id_with_stage_assignees_dto.stage_assignees
        ]
        return stage_ids

    @staticmethod
    def _validate_stage_ids(stage_ids, stage_ids_in_db):
        invalid_stage_ids = [
            stage_id for stage_id in stage_ids
            if stage_id not in stage_ids_in_db
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidDbStageIdsListException
            raise InvalidDbStageIdsListException(invalid_stage_ids)
        return

    @staticmethod
    def _check_duplicate_stage_ids(stage_ids: List[int]):

        length_of_stage_ids = len(stage_ids)
        duplicate_stage_ids = []
        for i in range(length_of_stage_ids):
            k = i + 1
            for j in range(k, length_of_stage_ids):
                if stage_ids[i] == stage_ids[j] and stage_ids[i] \
                        not in duplicate_stage_ids:
                    duplicate_stage_ids.append(stage_ids[i])

        if len(duplicate_stage_ids) != 0:
            raise DuplicateStageIds(duplicate_stage_ids=duplicate_stage_ids)
