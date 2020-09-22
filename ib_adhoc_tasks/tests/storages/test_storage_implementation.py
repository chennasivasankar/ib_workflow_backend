import pytest


class TestStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_adhoc_tasks.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    @pytest.mark.django_db
    def test_get_group_by_dtos_returns_group_by_response_dtos(
            self, storage
    ):
        # Arrange
        user_id = "user_id_1"
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        GroupByInfoFactory.reset_sequence(1)
        GroupByInfoFactory.create_batch(size=2, user_id=user_id)
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(1)
        group_by_response_dtos = GroupByResponseDTOFactory.create_batch(size=2)

        # Act
        actual_group_by_response_dtos = \
            storage.get_group_by_dtos(user_id="user_id_1")

        # Assert
        assert actual_group_by_response_dtos == group_by_response_dtos

    @pytest.mark.django_db
    def test_add_group_by_adds_group_by_and_returns_group_by_response_dto(
            self, storage
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            AddOrEditGroupByParameterDTOFactory
        AddOrEditGroupByParameterDTOFactory.reset_sequence(1)
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
            group_by_id=None
        )
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(1)
        group_by_response_dto = GroupByResponseDTOFactory()

        # Act
        actual_group_by_response_dto = storage.add_group_by(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )

        # Assert
        assert actual_group_by_response_dto == group_by_response_dto

    @pytest.mark.django_db
    def test_edit_group_by_adds_group_by_and_returns_group_by_response_dto(
            self, storage
    ):
        # Arrange
        group_by_id = 1
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        GroupByInfoFactory.reset_sequence(1)
        GroupByInfoFactory()
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            AddOrEditGroupByParameterDTOFactory
        AddOrEditGroupByParameterDTOFactory.reset_sequence(1)
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
            group_by_id=group_by_id, group_by_display_name="ASSIGNEE", order=2
        )
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(1)
        group_by_response_dto = GroupByResponseDTOFactory(
            group_by_display_name="ASSIGNEE", order=2
        )

        # Act
        actual_group_by_response_dto = storage.edit_group_by(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )

        # Assert
        assert actual_group_by_response_dto == group_by_response_dto
