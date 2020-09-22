import json

import pytest


class TestAddOrEditGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters.add_or_edit_group_by_presenter_implementation import \
            AddOrEditGroupByPresenterImplementation
        return AddOrEditGroupByPresenterImplementation()

    def test_get_response_for_add_or_edit_group_by_gives_response_dict(
            self, presenter
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(0)
        group_by_response_dto = GroupByResponseDTOFactory()
        expected_response_dict = {
            'group_by_display_name': 'ASSIGNEE',
            'group_by_id': 0,
            'order': 1
        }

        # Act
        http_response = presenter.get_response_for_add_or_edit_group_by(
            group_by_response_dto=group_by_response_dto
        )

        # Assert
        actual_response_dict = json.loads(http_response.content)
        assert actual_response_dict == expected_response_dict
