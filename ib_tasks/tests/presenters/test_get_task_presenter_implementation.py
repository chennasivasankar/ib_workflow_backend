import pytest


class TestGetTaskPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.get_task_presenter_implementation \
            import GetTaskPresenterImplementation
        presenter = GetTaskPresenterImplementation()
        return presenter

    @pytest.fixture
    def permission_task_gof_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFDTOFactory
        permission_task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
        ]
        return permission_task_gof_dtos

    @pytest.fixture
    def permission_task_gof_field_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskGoFFieldDTOFactory
        permission_task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response="response0"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3")
        ]
        return permission_task_gof_field_dtos

    @pytest.fixture
    def permission_task_details_dto(
            self, permission_task_gof_dtos, permission_task_gof_field_dtos
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            template_id="template0",
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=permission_task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def stage1_actions_dtos(self):
        from ib_tasks.interactors.storage_interfaces.actions_dtos \
            import ActionDTO
        actions_dtos = [
            ActionDTO(
                action_id="action1",
                name="action_name1",
                stage_id="stage1",
                button_text="button_text1",
                button_color="blue"
            ),
            ActionDTO(
                action_id="action2",
                name="action_name2",
                stage_id="stage1",
                button_text="button_text2",
                button_color="blue"
            ),
            ActionDTO(
                action_id="action3",
                name="action_name3",
                stage_id="stage1",
                button_text="button_text3",
                button_color="blue"
            )
        ]
        return actions_dtos

    @pytest.fixture
    def stage2_actions_dtos(self):
        from ib_tasks.interactors.storage_interfaces.actions_dtos \
            import ActionDTO
        actions_dtos = [
            ActionDTO(
                action_id="action1",
                name="action_name1",
                stage_id="stage2",
                button_text="button_text1",
                button_color="blue"
            ),
            ActionDTO(
                action_id="action2",
                name="action_name2",
                stage_id="stage2",
                button_text="button_text2",
                button_color="blue"
            ),
            ActionDTO(
                action_id="action3",
                name="action_name3",
                stage_id="stage2",
                button_text="button_text3",
                button_color="blue"
            )
        ]
        return actions_dtos

    @pytest.fixture
    def task_stage_complete_details_dto(
            self, stage1_actions_dtos, stage2_actions_dtos
    ):
        from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO
        stage_complete_details_dto = [
            StageAndActionsDetailsDTO(
                stage_id="stage1", name="stage_name1",
                actions_dtos=stage1_actions_dtos
            ),
            StageAndActionsDetailsDTO(
                stage_id="stage2", name="stage_name2",
                actions_dtos=stage2_actions_dtos
            )
        ]
        return stage_complete_details_dto

    @pytest.fixture
    def task_complete_details_dto(
            self, permission_task_details_dto,
            task_stage_complete_details_dto
    ):
        from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface \
            import TaskCompleteDetailsDTO
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_id="task0",
            task_details_dto=permission_task_details_dto,
            stages_and_actions_details_dtos=task_stage_complete_details_dto
        )
        return task_complete_details_dto

    def test_raise_exception_for_invalid_task_id(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        task_id = -1

        err = InvalidTaskIdException(task_id)

        # Act
        response_object = presenter.raise_exception_for_invalid_task_id(err)

        # Assert
        snapshot.assert_match(name="exception_object",
                              value=response_object.content)

    def test_given_task_complete_details_dto_returns_task_details(
            self, presenter, task_complete_details_dto, snapshot
    ):
        # Arrange

        # Act
        response_object = presenter.get_task_response(
            task_complete_details_dto)

        # Assert
        snapshot.assert_match(name="task_details = ",
                              value=response_object.content)
