import pytest


class TestCreateDiscussion:

    @pytest.fixture()
    def discussion_dto(self):
        from ib_discussions.interactors.dtos.dtos import \
            DiscussionWithEntityDetailsDTO
        from ib_discussions.constants.enum import EntityType
        discussion_dto = DiscussionWithEntityDetailsDTO(
            user_id="1",
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value,
            title="Interactor",
            description="test for interactor"
        )
        return discussion_dto

    @pytest.fixture()
    def service_interface(self):
        from ib_discussions.app_interfaces.service_interface import \
            ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    @pytest.mark.django_db
    def test_with_empty_title_raise_exception(self, discussion_dto,
                                              service_interface):
        # Arrange
        discussion_dto.title = ""

        # Assert
        from ib_discussions.interactors.discussion_interactor import EmptyTitle
        with pytest.raises(EmptyTitle):
            service_interface.create_discussion(
                discussion_with_entity_details_dto=discussion_dto)

    @pytest.mark.django_db
    def test_with_valid_details_create_discussion(self, discussion_dto,
                                                  service_interface):
        # Act
        service_interface.create_discussion(
            discussion_with_entity_details_dto=discussion_dto
        )

        # Assert
        from ib_discussions.models import DiscussionSet
        discussion_set_object = DiscussionSet.objects.get(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )
        from ib_discussions.models import Discussion
        discussion_object = Discussion.objects.filter(
            discussion_set_id=discussion_set_object.id
        ).first()

        assert discussion_object.title == discussion_dto.title
        assert discussion_object.description == discussion_dto.description
        assert discussion_object.user_id == discussion_object.user_id
