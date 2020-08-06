"""
Created on: 05/08/20
Author: Pavankumar Pamuru

"""
from unittest.mock import Mock

import pytest

from ib_tasks.interactors.filter_interactor import FilterInteractor


class TestFiltersInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
            FilterStorageInterface
        storage = FilterStorageInterface()
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface import \
            FilterPresenterInterface
        presenter = FilterPresenterInterface()
        return presenter

    @pytest.fixture
    def filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import CreateFilterDTOFactory
        CreateFilterDTOFactory.reset_sequence()
        return CreateFilterDTOFactory()

    @pytest.fixture
    def condition_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import \
            CreateConditionDTOFactory
        CreateConditionDTOFactory.reset_sequence()
        return CreateConditionDTOFactory.create_batch(3)

    def test_with_invalid_template_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos):
        # Arrange
        expected_response = Mock()
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        storage_mock.validate_template_id.side_effect = InvalidTemplateID
        presenter_mock.get_resonse_for_invalid_task_template_id.return_value = expected_response

        # Act

        actual_response = interactor.create_filter_wrapper(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        assert actual_response == expected_response

    def test_with_fields_not_belongs_to_template_id_return_error_message(
            self, storage_mock, presenter_mock, filter_dto, condition_dtos):
        # Arrange
        valid_field_ids = ['field_id_0']
        interactor = FilterInteractor(
            filter_storage=storage_mock,
            presenter=presenter_mock
        )

        from ib_tasks.exceptions.filter_exceptions import FieldIdsNotBelongsToTemplateId
        storage_mock.get_field_ids_for_task_template.return_value = valid_field_ids

        # Act
        with pytest.raises(FieldIdsNotBelongsToTemplateId) as error:
            interactor.create_filter_wrapper(
                filter_dto=filter_dto,
                condition_dtos=condition_dtos
            )
