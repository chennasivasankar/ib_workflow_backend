import pytest




class TestSearchableFieldValuesInteractor:
    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            searchable_field_values_presenter_interface import \
            SearchableFieldValuesPresenterInterface
        from mock import create_autospec
        presenter = create_autospec(SearchableFieldValuesPresenterInterface)
        return presenter

    @pytest.fixture()
    def elastic_storage_mock(self):
        from mock import create_autospec
        from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
            ElasticSearchStorageInterface
        storage = create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.mark.parametrize("limit", [0, -1])
    def test_given_limit_values_less_than_one_raise_exception(
            self, limit, presenter_mock, elastic_storage_mock):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            SearchableFieldTypeDTOFactory
        searchable_field_type_dto = SearchableFieldTypeDTOFactory(limit=limit)

        from ib_tasks.exceptions.fields_custom_exceptions import \
            LimitShouldBeGreaterThanZeroException
        presenter_mock.raise_limit_should_be_greater_than_zero_exception. \
            side_effect = LimitShouldBeGreaterThanZeroException
        from ib_tasks.interactors.searchable_field_values_interactor import \
            SearchableFieldValuesInteractor
        interactor = SearchableFieldValuesInteractor()

        # Act
        with pytest.raises(LimitShouldBeGreaterThanZeroException):
            interactor.searchable_field_values_wrapper(
                presenter=presenter_mock,
                searchable_field_type_dto=searchable_field_type_dto)
        # Assert
        presenter_mock.raise_limit_should_be_greater_than_zero_exception.assert_called_once(
        )

    @pytest.mark.parametrize("offset", [-2, -3])
    def test_given_offset_values_less_than_minus_one_raise_exception(
            self, offset, presenter_mock, elastic_storage_mock):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos import \
            SearchableFieldTypeDTOFactory
        searchable_field_type_dto = SearchableFieldTypeDTOFactory(
            offset=offset)
        from ib_tasks.exceptions.fields_custom_exceptions import \
            OffsetShouldBeGreaterThanOrEqualToMinusOneException
        presenter_mock.\
            raise_offset_should_be_greater_than_or_equal_to_minus_one_exception\
            .side_effect = OffsetShouldBeGreaterThanOrEqualToMinusOneException
        from ib_tasks.interactors.searchable_field_values_interactor import \
            SearchableFieldValuesInteractor
        interactor = SearchableFieldValuesInteractor()

        # Act
        with pytest.raises(
                OffsetShouldBeGreaterThanOrEqualToMinusOneException):
            interactor.searchable_field_values_wrapper(
                presenter=presenter_mock,
                searchable_field_type_dto=searchable_field_type_dto)
        # Assert
        presenter_mock. \
            raise_offset_should_be_greater_than_or_equal_to_minus_one_exception \
            .assert_called_once()

    def test_get_searchable_field_value_details_given_valid_user_details(
            self, mocker, presenter_mock, elastic_storage_mock):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos import \
            SearchableFieldTypeDTOFactory
        searchable_field_type_dto = SearchableFieldTypeDTOFactory(offset=0,
                                                                  limit=1)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_based_on_limit_and_offset_mock
        get_user_dtos_based_on_limit_and_offset_mock_method = \
            get_user_dtos_based_on_limit_and_offset_mock(mocker)
        searchable_user_detail_dtos = get_user_dtos_based_on_limit_and_offset_mock_method(
        )

        from ib_tasks.interactors.searchable_field_values_interactor import \
            SearchableFieldValuesInteractor
        interactor = SearchableFieldValuesInteractor()

        interactor.searchable_field_values_wrapper(
            presenter=presenter_mock,
            searchable_field_type_dto=searchable_field_type_dto)
        get_user_dtos_based_on_limit_and_offset_mock_method.asser_called_once()
        presenter_mock.get_searchable_field_values_response.assert_called_once_with(
            searchable_user_detail_dtos)

    def test_get_searchable_field_value_details_given_valid_user_details_and_offset_one(
            self, mocker, presenter_mock, elastic_storage_mock):
        # Arrange

        from ib_tasks.tests.factories.interactor_dtos import \
            SearchableFieldTypeDTOFactory
        searchable_field_type_dto = SearchableFieldTypeDTOFactory(offset=-1)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_all_user_dtos_based_on_query_mock
        get_all_user_dtos_based_on_query_mock_method = \
            get_all_user_dtos_based_on_query_mock(mocker)
        searchable_user_detail_dtos = \
            get_all_user_dtos_based_on_query_mock_method()

        from ib_tasks.interactors.searchable_field_values_interactor import \
            SearchableFieldValuesInteractor
        interactor = SearchableFieldValuesInteractor()

        interactor.searchable_field_values_wrapper(
            presenter=presenter_mock,
            searchable_field_type_dto=searchable_field_type_dto)
        get_all_user_dtos_based_on_query_mock_method.asser_called_once()
        presenter_mock.get_searchable_field_values_response. \
            assert_called_once_with(searchable_user_detail_dtos)
