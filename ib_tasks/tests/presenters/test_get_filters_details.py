

class TestGetFiltersDetailsPresenter:

    @staticmethod
    def test_get_filter_details(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        user_id = '1'
        from ib_tasks.tests.factories.storage_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filters = FilterDTOFactory.create_batch(2, user_id=user_id)
        from ib_tasks.tests.factories.storage_dtos import ConditionDTOFactory
        ConditionDTOFactory.reset_sequence(1)
        conditions = ConditionDTOFactory.create_batch(2)
        from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO
        filter_details = FilterCompleteDetailsDTO(
            filters_dto=filters, conditions_dto=conditions
        )
        import json

        # Act
        response_object = presenter.get_response_for_get_filters_details(
            filter_complete_details=filter_details
        )

        # Assert
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_update_filter_status(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        import json
        filter_id = 1
        from ib_tasks.constants.enum import Status
        is_selected = Status.ENABLED.value

        # Act
        response_object = presenter.get_response_for_update_filter_status(
            filter_id=filter_id, is_selected=is_selected
        )

        # Assert
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_raises_exception(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        import json
        filter_id = 1
        from ib_tasks.constants.enum import Status
        is_selected = Status.ENABLED.value

        # Act
        response_object = \
            presenter.get_response_for_invalid_user_to_update_filter_status()

        # Assert
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )