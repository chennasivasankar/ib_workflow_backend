from ib_tasks.presenters.get_task_rps_presenter_implementation import \
    GetTaskRpsPresenterImplementation


class TestGetTaskRelatedRps:
    def test_response_invalid_task_id(self, snapshot):
        # Arrange
        presenter = GetTaskRpsPresenterImplementation()
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId
        task_id = "iBWF-10"

        err = InvalidTaskDisplayId(task_id)

        # Act
        response_object = presenter.response_for_invalid_task_id(err)

        # Assert
        snapshot.assert_match(response_object.content, "response")

    def test_response_for_user_is_not_assignee_for_task(self, snapshot):
        # Arrange
        presenter = GetTaskRpsPresenterImplementation()

        # Act
        response_object = presenter.response_for_user_is_not_assignee_for_task()

        # Assert
        snapshot.assert_match(response_object.content, "response")

    def test_response_for_invalid_stage_id(self, snapshot):
        # Arrange
        presenter = GetTaskRpsPresenterImplementation()

        # Act
        response_object = presenter.response_for_invalid_stage_id()

        # Assert
        snapshot.assert_match(response_object.content, "response")

    def test_response_for_get_task_rps_details(self, snapshot):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import UserDetailsDTOFactory
        UserDetailsDTOFactory.reset_sequence()
        rp_dtos = UserDetailsDTOFactory.create_batch(size=4)
        presenter = GetTaskRpsPresenterImplementation()

        # Act
        response_object = presenter.response_for_get_rps_details(rp_dtos)

        # Assert
        snapshot.assert_match(response_object.content, "response")
