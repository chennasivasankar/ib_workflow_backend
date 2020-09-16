from typing import List

from ib_tasks.exceptions.adapter_exceptions \
    import InvalidProjectIdsException, UserIsNotInProjectException
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateDBId
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.presenter_interfaces.get_template_stage_flow_presenter_interface import \
    GetTemplateStageFlowPresenterInterface, StageFlowCompleteDetailsDTO
from ib_tasks.interactors.stages_dtos import StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface


class GetPermittedTemplateStageFlowToUser(ValidationMixin):
    def __init__(
            self, template_storage: TaskTemplateStorageInterface,
            stage_storage: StageStorageInterface,
            action_storage: ActionStorageInterface
    ):
        self.template_storage = template_storage
        self.stage_storage = stage_storage
        self.action_storage = action_storage

    def get_permitted_template_stage_flow_to_user_wrapper(
            self, user_id: str, project_id: str,
            template_id: str,
            presenter: GetTemplateStageFlowPresenterInterface
    ):
        try:
            template_stage_flow_dtos = \
                self._get_permitted_template_stage_flow_to_user(
                    user_id=user_id, template_id=template_id,
                    project_id=project_id
                )
        except InvalidTaskTemplateDBId as err:
            return presenter.raise_invalid_task_template_id(err=err)
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_not_in_project()
        return presenter.get_response_for_template_stage_flow(
            stage_flow_complete_details_dto=template_stage_flow_dtos
        )

    def _get_permitted_template_stage_flow_to_user(
            self, user_id: str, template_id: str, project_id: str
    ) -> StageFlowCompleteDetailsDTO:
        self._validations_for_input_data(
            template_id=template_id, project_id=project_id, user_id=user_id
        )
        user_roles = self._get_user_roles_in_project(
            user_id=user_id, project_id=project_id
        )
        stage_dtos = self.stage_storage.get_user_permitted_stages_in_template(
            template_id=template_id, user_roles=user_roles
        )
        stage_ids = self._get_stage_ids(stage_dtos=stage_dtos)
        action_ids = \
            self.action_storage.get_user_permitted_action_ids_given_stage_ids(
                user_roles=user_roles, stage_ids=stage_ids
            )
        return self._get_stage_flow_complete_details_dto(
            stage_ids=stage_ids, action_ids=action_ids,
            stage_dtos=stage_dtos
        )

    @staticmethod
    def _get_stage_ids(stage_dtos: List[StageMinimalDTO]) -> List[int]:

        return [
            stage_dto.stage_id
            for stage_dto in stage_dtos
        ]

    @staticmethod
    def _get_user_roles_in_project(user_id: str,
                                   project_id: str) -> List[str]:
        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter().roles_service
        user_roles = adapter.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )
        return user_roles

    def _validations_for_input_data(self, template_id: str,
                                    project_id: str,
                                    user_id: str):
        self.validate_given_project_ids(
            project_ids=[project_id]
        )
        self.validate_if_user_is_in_project(
            user_id=user_id, project_id=project_id
        )
        invalid_template = not self.template_storage.check_is_template_exists(
            template_id=template_id
        )
        if invalid_template:
            raise InvalidTaskTemplateDBId(invalid_task_template_id=template_id)

    def get_template_stage_flow_to_user_wrapper(
            self, user_id: str, project_id: str,
            template_id: str,
            presenter: GetTemplateStageFlowPresenterInterface
    ):
        try:
            template_stage_flow_dtos = \
                self._get_template_stage_flow_to_user(
                    user_id=user_id, template_id=template_id,
                    project_id=project_id
                )
        except InvalidTaskTemplateDBId as err:
            return presenter.raise_invalid_task_template_id(err=err)
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_not_in_project()
        return presenter.get_response_for_template_stage_flow(
            stage_flow_complete_details_dto=template_stage_flow_dtos
        )

    def _get_template_stage_flow_to_user(
            self, user_id: str, template_id: str, project_id: str
    ) -> StageFlowCompleteDetailsDTO:
        self._validations_for_input_data(
            template_id=template_id, project_id=project_id, user_id=user_id
        )
        stage_dtos = self.stage_storage.get_stages_in_template(
            template_id=template_id
        )
        stage_ids = self._get_stage_ids(stage_dtos=stage_dtos)
        action_ids = \
            self.action_storage.get_action_ids_given_stage_ids(
                stage_ids=stage_ids
            )
        return self._get_stage_flow_complete_details_dto(
            stage_ids=stage_ids, action_ids=action_ids,
            stage_dtos=stage_dtos
        )

    def _get_stage_flow_complete_details_dto(
            self, stage_ids: List[int],
            action_ids: List[int],
            stage_dtos: List[StageMinimalDTO]
    ) -> StageFlowCompleteDetailsDTO:

        stage_flow_dtos = self.stage_storage.get_stage_flows_to_user(
            stage_ids=stage_ids, action_ids=action_ids
        )
        return StageFlowCompleteDetailsDTO(
            stage_dtos=stage_dtos,
            stage_flow_dtos=stage_flow_dtos
        )