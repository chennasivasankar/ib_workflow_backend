class TestSearchableFieldValuesPresenterImplementation:
    def test_raise_exception_for_limit_less_than_zero(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            LIMIT_SHOULD_BE_GREATER_THAN_ZERO
        expected_response = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[0]
        response_status_code = LIMIT_SHOULD_BE_GREATER_THAN_ZERO[1]
        from ib_tasks.presenters. \
            searchable_field_values_presenter_implementation import \
            SearchableFieldValuesPresenterImplementation
        presenter = SearchableFieldValuesPresenterImplementation()
        # Act
        response_object = presenter. \
            raise_limit_should_be_greater_than_zero_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_exception_for_offset_less_than_minus_one(self):
        # Arrange
        from ib_tasks.constants.exception_messages import \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE
        expected_response = \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE[0]
        response_status_code = \
            OFFSET_SHOULD_BE_GREATER_THAN_OR_EQUAL_TO_MINUS_ONE[1]
        from ib_tasks.presenters. \
            searchable_field_values_presenter_implementation import \
            SearchableFieldValuesPresenterImplementation
        presenter = SearchableFieldValuesPresenterImplementation()
        # Act
        response_object = presenter. \
            raise_offset_should_be_greater_than_or_equal_to_minus_one_exception()
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response['http_status_code'] == 400
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_get_user_searchable_field_values_given_user_searchable_field_dtos(
            self):
        # Arrange
        searchable_value_details = [{
            'id': 'user_1',
            'name': 'user_name_1'
        }, {
            'id': 'user_2',
            'name': 'user_name_2'
        }]
        from ib_tasks.tests.factories.interactor_dtos import\
            SearchableFieldUserDetailDTOFactory
        SearchableFieldUserDetailDTOFactory.reset_sequence()
        searchable_value_detail_dtos = SearchableFieldUserDetailDTOFactory. \
            create_batch(2)

        from ib_tasks.presenters. \
            searchable_field_values_presenter_implementation import \
            SearchableFieldValuesPresenterImplementation
        presenter = SearchableFieldValuesPresenterImplementation()
        # Act
        response_object = presenter. \
            get_searchable_field_values_response(searchable_value_detail_dtos)
        # Assert
        import json
        response = json.loads(response_object.content)
        assert response == searchable_value_details
