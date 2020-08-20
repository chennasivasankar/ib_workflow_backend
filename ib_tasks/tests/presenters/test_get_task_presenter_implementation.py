import pytest

from ib_tasks.tests.factories.interactor_dtos import \
    StageAssigneeDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import StageActionDetailsDTOFactory, \
    TaskGoFDTOFactory, TaskGoFFieldDTOFactory, StageAssigneeDTOFactory
from ib_tasks.tests.factories.adapter_dtos import \
            AssigneeDetailsDTOFactory


class TestGetTaskPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.get_task_presenter_implementation \
            import GetTaskPresenterImplementation
        presenter = GetTaskPresenterImplementation()
        return presenter

    @pytest.fixture
    def task_base_details_dto(self):
        from ib_tasks.tests.factories.storage_dtos import \
            TaskBaseDetailsDTOFactory
        task_base_details_dto = TaskBaseDetailsDTOFactory()
        return task_base_details_dto

    @pytest.fixture
    def reset_sequence(self):
        TaskGoFDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()
        StageAssigneeDTOFactory.reset_sequence()
        StageAssigneeDetailsDTOFactory.reset_sequence()

    @pytest.fixture
    def permission_task_gof_dtos(self):
        permission_task_gof_dtos = [
            TaskGoFDTOFactory(task_gof_id=0, gof_id="gof0", same_gof_order=0),
            TaskGoFDTOFactory(task_gof_id=1, gof_id="gof1", same_gof_order=0),
        ]
        return permission_task_gof_dtos

    @pytest.fixture
    def permission_task_gof_field_dtos(self):
        permission_task_gof_field_dtos = [
            TaskGoFFieldDTOFactory(task_gof_id=0, field_id="field0",
                                   field_response='{"id": 1, "value": "Hyderabad"}'),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field2",
                                   field_response="response2"),
            TaskGoFFieldDTOFactory(task_gof_id=1, field_id="field3",
                                   field_response="response3")
        ]
        return permission_task_gof_field_dtos

    @pytest.fixture
    def permission_task_details_dto(
            self, permission_task_gof_dtos, permission_task_gof_field_dtos,
            task_base_details_dto
    ):
        from ib_tasks.interactors.storage_interfaces.get_task_dtos \
            import TaskDetailsDTO
        task_details_dto = TaskDetailsDTO(
            task_base_details_dto=task_base_details_dto,
            task_gof_dtos=permission_task_gof_dtos,
            task_gof_field_dtos=permission_task_gof_field_dtos
        )
        return task_details_dto

    @pytest.fixture
    def stages_action_dtos(self):
        from ib_tasks.constants.enum import ValidationType
        stages_action_dtos = [
            StageActionDetailsDTOFactory(
                stage_id="stage0",
                action_type=ValidationType.NO_VALIDATIONS.value
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage0",
                action_type=None
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage1",
                action_type=ValidationType.NO_VALIDATIONS.value
            ),
            StageActionDetailsDTOFactory(
                stage_id="stage1",
                action_type=None
            ),
        ]
        return stages_action_dtos

    @pytest.fixture
    def stages_and_actions_details_dtos(self, stages_action_dtos):
        from ib_tasks.interactors.task_dtos import StageAndActionsDetailsDTO
        stages_and_actions_details_dtos = [
            StageAndActionsDetailsDTO(
                stage_id="stage0",
                name="name1",
                db_stage_id=1,
                color="color1",
                actions_dtos=[stages_action_dtos[0], stages_action_dtos[1]]
            ),
            StageAndActionsDetailsDTO(
                stage_id="stage1",
                name="name2",
                db_stage_id=2,
                color="color2",
                actions_dtos=[stages_action_dtos[2], stages_action_dtos[3]]
            ),
            StageAndActionsDetailsDTO(
                stage_id="stage2",
                name="name3",
                db_stage_id=3,
                color="color3",
                actions_dtos=[]
            )
        ]
        return stages_and_actions_details_dtos

    @pytest.fixture
    def assignee_details_dtos(self):
        assignee_details_dtos = [
            AssigneeDetailsDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174001")
        ]
        return assignee_details_dtos

    @pytest.fixture
    def stage_assignee_dtos(self):
        stage_assignee_dtos = [
            StageAssigneeDTOFactory(
                assignee_id="123e4567-e89b-12d3-a456-426614174001"),
            StageAssigneeDTOFactory(assignee_id=None),
            StageAssigneeDTOFactory(assignee_id=None)
        ]
        return stage_assignee_dtos

    @pytest.fixture
    def stage_assignee_details_dtos(
            self, assignee_details_dtos, stage_assignee_dtos
    ):
        stage_assignee_details_dtos = [
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[0].task_stage_id,
                stage_id=stage_assignee_dtos[0].stage_id,
                assignee_details_dto=assignee_details_dtos[0]),
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[1].task_stage_id,
                stage_id=stage_assignee_dtos[1].stage_id,
                assignee_details_dto=None),
            StageAssigneeDetailsDTOFactory(
                task_stage_id=stage_assignee_dtos[2].task_stage_id,
                stage_id=stage_assignee_dtos[2].stage_id,
                assignee_details_dto=None),

        ]
        return stage_assignee_details_dtos

    @pytest.fixture
    def task_complete_details_dto(
            self, permission_task_details_dto,
            stages_and_actions_details_dtos,
            stage_assignee_details_dtos
    ):
        from ib_tasks.interactors.presenter_interfaces \
            .get_task_presenter_interface \
            import TaskCompleteDetailsDTO
        task_complete_details_dto = TaskCompleteDetailsDTO(
            task_details_dto=permission_task_details_dto,
            stages_and_actions_details_dtos=stages_and_actions_details_dtos,
            stage_assignee_details_dtos=stage_assignee_details_dtos
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

    def test_raise_user_permission_denied(self, presenter, snapshot):
        # Arrange

        # Act
        response_object = presenter.raise_user_permission_denied()

        # Assert
        snapshot.assert_match(name="exception_object",
                              value=response_object.content)

    def test_raise_exception_for_invalid_task_display_id(
            self, presenter, snapshot
    ):
        # Arrange
        task_display_id = "IBWF-10"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        err = InvalidTaskDisplayId(task_display_id)

        # Act
        response_object = presenter.raise_invalid_task_display_id(err)

        # Assert
        snapshot.assert_match(name="exception_object",
                              value=response_object.content)

    def test_raise_exception_for_raise_invalid_stage_ids_for_task(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStageIdsForTask
        message = "invaild stage ids"
        err = InvalidStageIdsForTask(message)

        # Act
        response_object = presenter.raise_invalid_stage_ids_for_task(err)

        # Assert
        snapshot.assert_match(name="exception_object",
                              value=response_object.content)

    def test_raise_exception_for_invalid_city_ids(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidCityIdsException
        city_ids = [100, 110]
        err = InvalidCityIdsException(city_ids)

        # Act
        response_object = presenter.raise_invalid_city_ids(err)

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response_object.content
        )

    def test_raise_exception_for_invalid_state_ids(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStateIdsException
        state_ids = [100, 110]
        err = InvalidStateIdsException(state_ids)

        # Act
        response_object = presenter.raise_invalid_state_ids(err)

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response_object.content
        )

    def test_raise_exception_for_invalid_country_ids(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidCountryIdsException
        country_ids = [10, 11]
        err = InvalidCountryIdsException(country_ids)

        # Act
        response_object = presenter.raise_invalid_country_ids(err)

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response_object.content
        )

    def test_raise_exception_for_invalid_user_ids(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidUserIdsException
        user_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001"
        ]
        err = InvalidUserIdsException(user_ids)

        # Act
        response_object = presenter.raise_invalid_user_ids(err)

        # Assert
        snapshot.assert_match(
            name="exception_object",
            value=response_object.content
        )

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
