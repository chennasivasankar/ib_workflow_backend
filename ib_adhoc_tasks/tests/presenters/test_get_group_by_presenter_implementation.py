import json

import pytest


class TestGetGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters.get_group_by_presenter_implementation import \
            GetGroupByPresenterImplementation
        return GetGroupByPresenterImplementation()

    def test_get_response_for_get_group_by_gives_response_dict(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupByResponseDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        group_by_response_dtos = \
            GroupByResponseDTOFactory.create_batch(size=2)

        # Act
        http_response = presenter.get_response_for_get_group_by(
            group_by_response_dtos=group_by_response_dtos
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "group_by_response_dict")
