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

    @pytest.mark.parametrize("limit", [0, -1])
    def test_given_limit_values_less_than_one_raise_exception(
            self, limit, presenter_mock):
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
            self, offset, presenter_mock):
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
        presenter_mock.\
            raise_offset_should_be_greater_than_or_equal_to_minus_one_exception\
            .assert_called_once()

