
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
    def test_create_filter_details(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        user_id = '1'
        from ib_tasks.tests.factories.filter_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filter_dto = FilterDTOFactory()
        from ib_tasks.tests.factories.filter_dtos import ConditionDTOFactory
        ConditionDTOFactory.reset_sequence(1)
        condition_dtos = ConditionDTOFactory.create_batch(2)

        # Act
        response_object = presenter.get_response_for_create_filter(
            filter_dto=filter_dto, condition_dtos=condition_dtos
        )

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_update_filter_details(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        user_id = '1'
        from ib_tasks.tests.factories.filter_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence(1)
        filter_dto = FilterDTOFactory()
        from ib_tasks.tests.factories.filter_dtos import ConditionDTOFactory
        ConditionDTOFactory.reset_sequence(1)
        condition_dtos = ConditionDTOFactory.create_batch(2)

        # Act
        response_object = presenter.get_response_for_update_filter(
            filter_dto=filter_dto, condition_dtos=condition_dtos
        )

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_invalid_filter_id(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()

        # Act
        response_object = presenter.get_response_for_invalid_filter_id()

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_invalid_user_to_update_filter_status(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()

        # Act
        response_object = presenter.\
            get_response_for_invalid_user_to_update_filter_status()

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_invalid_task_template_id(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()

        # Act
        response_object = presenter. \
            get_response_for_invalid_task_template_id()

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_invalid_field_ids(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        from ib_tasks.exceptions.filter_exceptions import \
            FieldIdsNotBelongsToTemplateId

        # Act
        response_object = presenter. \
            get_response_for_invalid_field_ids(
                error=FieldIdsNotBelongsToTemplateId(field_ids=[1, 2])
            )

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_user_not_have_access_to_fields(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        from ib_tasks.exceptions.filter_exceptions import \
            FieldIdsNotBelongsToTemplateId

        # Act
        response_object = presenter. \
            get_response_for_user_not_have_access_to_fields()

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_user_not_have_access_to_update_filter(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        from ib_tasks.exceptions.filter_exceptions import \
            FieldIdsNotBelongsToTemplateId

        # Act
        response_object = presenter. \
            get_response_for_user_not_have_access_to_update_filter()

        # Assert
        import json
        snapshot.assert_match(
            name="filters", value=json.loads(response_object.content)
        )

    @staticmethod
    def test_get_response_for_user_not_have_access_to_delete_filter(snapshot):
        # Arrange
        from ib_tasks.presenters.filter_presenter_implementation \
            import FilterPresenterImplementation
        presenter = FilterPresenterImplementation()
        from ib_tasks.exceptions.filter_exceptions import \
            FieldIdsNotBelongsToTemplateId

        # Act
        response_object = presenter. \
            get_response_for_user_not_have_access_to_delete_filter()

        # Assert
        import json
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