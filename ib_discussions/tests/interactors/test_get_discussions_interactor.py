'''
request - entity-id, entity_type, offset, limit

# TODO
1. validate offset
2. validate limit
3. validate the entity id
4. validate the entity type for entity id
5. get discussion_set_id for entity id and entity type
6. get discussion_dto for discussion_set_id
7. get total discussions count
8. get user details
'''
from unittest.mock import Mock

import pytest


class TestGetDiscussionsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_discussions.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_discussions.interactors.presenter_interfaces.presenter_interface \
            import PresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(PresenterInterface)
        return presenter

    def test_validate_offset_value_raise_exception(self, storage_mock,
                                                   presenter_mock):
        # Arrange
        entity_id = "6a76277b-fb73-4920-a79d-4c65814f9de5"
        offset = -1
        limit = 1
        expected_presenter_raise_exception_for_invalid_offset_mock = Mock()
        from ib_discussions.constants.enum import EntityType
        entity_type = EntityType.TASK.value

        presenter_mock.raise_exception_for_invalid_offset.return_value \
            = expected_presenter_raise_exception_for_invalid_offset_mock

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)

        # Act
        response_object = interactor.get_discussions_wrapper(
            entity_id=entity_id, entity_type=entity_type, offset=offset,
            limit=limit
        )

        # Assert
        assert response_object \
               == expected_presenter_raise_exception_for_invalid_offset_mock
