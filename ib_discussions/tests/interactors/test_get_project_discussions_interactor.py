from unittest.mock import Mock

import pytest


class TestGetProjectDiscussionsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_discussions.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
            GetProjectDiscussionsPresenterInterface
        presenter = create_autospec(GetProjectDiscussionsPresenterInterface)
        return presenter

    @pytest.fixture()
    def entity_id_and_entity_type_dto(self):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.interactors.dtos.dtos import \
            EntityIdAndEntityTypeDTO
        entity_id_and_entity_type_dto = EntityIdAndEntityTypeDTO(
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value
        )
        return entity_id_and_entity_type_dto

    @pytest.fixture()
    def offset_and_limit_dto(self):
        from ib_discussions.interactors.dtos.dtos import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=0,
            limit=3
        )
        return offset_and_limit_dto

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.get_project_discussions_interactor import \
            GetProjectDiscussionInteractor
        interactor = GetProjectDiscussionInteractor(storage=storage_mock)
        return interactor

    @pytest.fixture()
    def filter_by_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            FilterByDTOFactory
        FilterByDTOFactory.filter_by.reset()
        FilterByDTOFactory.value.reset()
        filter_by_dto = FilterByDTOFactory.create()
        return filter_by_dto

    @pytest.fixture()
    def sort_by_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            SortByDTOFactory
        SortByDTOFactory.sort_by.reset()
        SortByDTOFactory.order.reset()
        sort_by_dto = SortByDTOFactory()
        return sort_by_dto

    @pytest.fixture()
    def get_discussion_dtos(self, discussion_set_id):
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        complete_discussion_dtos = DiscussionDTOFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id
        )
        return complete_discussion_dtos

    @pytest.fixture()
    def get_user_profile_dtos(self):
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = UserProfileDTOFactory.create_batch(size=3)
        return user_profile_dtos

    def test_validate_offset_value_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto,
            offset_and_limit_dto, interactor,
            filter_by_dto, sort_by_dto
    ):
        # Arrange
        project_id = "FIN_MAN"
        offset_and_limit_dto.offset = -1
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"

        expected_presenter_raise_exception_for_invalid_offset_mock = Mock()

        presenter_mock.response_for_invalid_offset.return_value \
            = expected_presenter_raise_exception_for_invalid_offset_mock

        # Act
        response = interactor.get_project_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock,
            sort_by_dto=sort_by_dto, filter_by_dto=filter_by_dto,
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response \
               == expected_presenter_raise_exception_for_invalid_offset_mock

        presenter_mock.response_for_invalid_offset.assert_called_once()
