
import pytest
from unittest.mock import create_autospec
from ib_tasks.interactors.configur_initial_task_template_stage_actions import (
    ConfigureInitialTaskTemplateStageActions, InvalidTaskTemplateIdsException
)
from ib_tasks.interactors.stages_dtos import TemplateStageDTO
from ib_tasks.tests.factories.interactor_dtos \
    import TaskTemplateStageActionDTOFactory


class TestConfigureInitialTaskTemplateStageActions:

    @pytest.fixture()
    def action_storage(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface \
            import ActionStorageInterface
        storage = create_autospec(ActionStorageInterface)
        return storage

    @pytest.fixture()
    def template_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
            import TaskTemplateStorageInterface
        storage = create_autospec(TaskTemplateStorageInterface)
        return storage


    @staticmethod
    def test_given_invalid_task_template_ids_raises_exception(
            action_storage, template_storage):

        # Arrange
        import pytest
        import json
        project_id = "FINMAN"
        expected_task_template_ids = ["task_template_2"]
        expected_task_template_ids_dict = json.dumps(
            {"invalid_task_template_ids": expected_task_template_ids}
        )
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)

        task_template_ids = ["task_template_1", "task_template_2"]

        action_storage.get_valid_task_template_ids\
            .return_value = ["task_template_1"]

        interactor = ConfigureInitialTaskTemplateStageActions(
            storage=action_storage,
            template_storage=template_storage,
            tasks_dto=tasks_dto
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIdsException) as err:
            assert interactor\
                .create_update_delete_stage_actions_to_task_template(
                project_id=project_id
            )

        # Assert
        assert \
            err.value.task_template_ids_dict == expected_task_template_ids_dict
        action_storage.get_valid_task_template_ids\
            .assert_called_once_with(task_template_ids=task_template_ids)

    @staticmethod
    def test_given_more_than_one_stage_to_task_template_raises_exception(
            action_storage, template_storage):
        # Arrange
        project_id = "FINMAN"
        import pytest
        import json
        expected_task_template_stages_dict = json.dumps(
            {"task_template_1": ['stage_1', 'stage_3']}
        )
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        tasks_dto.append(TaskTemplateStageActionDTOFactory(
            task_template_id='task_template_1')
        )

        task_template_ids = ["task_template_1", "task_template_2"]
        action_storage.get_valid_task_template_ids\
            .return_value = task_template_ids

        interactor = ConfigureInitialTaskTemplateStageActions(
            storage=action_storage,
            template_storage=template_storage,
            tasks_dto=tasks_dto
        )
        from ib_tasks.exceptions.task_custom_exceptions \
            import ManyStagesToInitialTaskTemplate

        # Act
        with pytest.raises(ManyStagesToInitialTaskTemplate) as err:
            assert interactor\
                .create_update_delete_stage_actions_to_task_template(
                project_id=project_id
            )

        # Assert
        assert err.value.task_template_stages_dict == \
               expected_task_template_stages_dict
        action_storage.get_valid_task_template_ids \
            .assert_called_once_with(task_template_ids=task_template_ids)

    @staticmethod
    def test_given_valid_details_creates_stage_actions_to_task_template(
            mocker, action_storage, template_storage):

        # Arrange
        project_id = "FINMAN"
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)

        task_template_ids = ["task_template_1", "task_template_2"]
        action_storage.get_valid_task_template_ids\
            .return_value = task_template_ids
        task_template_stage_dtos = [
            TemplateStageDTO(
                task_template_id="task_template_1",
                stage_id="stage_1"
            ),
            TemplateStageDTO(
                task_template_id="task_template_2",
                stage_id="stage_2"
            )
        ]
        path = 'ib_tasks.interactors.create_or_update_or_delete_stage_actions.CreateOrUpdateOrDeleteStageActions' \
               '.create_or_update_or_delete_stage_actions'
        mock_obj = mocker.patch(path)

        interactor = ConfigureInitialTaskTemplateStageActions(
            storage=action_storage,
            template_storage=template_storage,
            tasks_dto=tasks_dto
        )

        # Act
        interactor.create_update_delete_stage_actions_to_task_template(
            project_id=project_id
        )

        # Assert

        action_storage.get_valid_task_template_ids \
            .assert_called_once_with(task_template_ids=task_template_ids)
        action_storage.create_initial_stage_to_task_template.assert_called_once_with(
            task_template_stage_dtos=task_template_stage_dtos
        )
        mock_obj.called_once()
