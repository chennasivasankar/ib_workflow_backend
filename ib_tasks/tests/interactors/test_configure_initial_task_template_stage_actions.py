
from unittest.mock import create_autospec

from ib_tasks.interactors.stages_dtos import TaskTemplateStageDTO
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface

from ib_tasks.interactors.configur_initial_task_template_stage_actions \
    import (
        ConfigureInitialTaskTemplateStageActions,
        InvalidTaskTemplateIdsException
    )
from ib_tasks.tests.factories.interactor_dtos \
    import TaskTemplateStageActionDTOFactory


class TestConfigureInitialTaskTemplateStageActions:

    @staticmethod
    def test_given_invalid_task_template_ids_raises_exception():
        # Arrange
        import pytest
        import json
        expected_task_template_ids = ["task_template_2"]
        expected_task_template_ids_dict = json.dumps(
            {"invalid_task_template_ids": expected_task_template_ids}
        )
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)

        task_template_ids = ["task_template_1", "task_template_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_task_template_ids.return_value = ["task_template_1"]

        interactor = ConfigureInitialTaskTemplateStageActions(
            storage=storage,
            tasks_dto=tasks_dto
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIdsException) as err:
            assert interactor\
                .create_update_delete_stage_actions_to_task_template()

        # Assert
        assert \
            err.value.task_template_ids_dict == expected_task_template_ids_dict
        storage.get_valid_task_template_ids\
            .assert_called_once_with(task_template_ids=task_template_ids)

    @staticmethod
    def test_given_valid_details_creates_stage_actions_to_task_template(mocker):

        # Arrange
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)

        task_template_ids = ["task_template_1", "task_template_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_task_template_ids.return_value = task_template_ids
        task_template_stage_dtos = [
            TaskTemplateStageDTO(
                task_template_id="task_template_1",
                stage_id="stage_1"
            ),
            TaskTemplateStageDTO(
                task_template_id="task_template_2",
                stage_id="stage_2"
            )
        ]

        mock_obj = mocker.patch('ib_tasks.interactors.create_update_delete_stage_actions.CreateUpdateDeleteStageActionsInteractor.create_update_delete_stage_actions')

        interactor = ConfigureInitialTaskTemplateStageActions(
            storage=storage,
            tasks_dto=tasks_dto
        )

        # Act
        interactor.create_update_delete_stage_actions_to_task_template()

        # Assert

        storage.get_valid_task_template_ids \
            .assert_called_once_with(task_template_ids=task_template_ids)
        storage.create_initial_stage_to_task_template.assert_called_once_with(
            task_template_stage_dtos=task_template_stage_dtos
        )
        mock_obj.called_once()
