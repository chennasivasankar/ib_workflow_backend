import pytest


class TestStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_adhoc_tasks.storages.storage_implementation import \
            StorageImplementation
        return StorageImplementation()

    # @pytest.mark.django_db
    # def test_get_group_by_dtos_returns_group_by_response_dtos(
    #         self, storage
    # ):
    #     # Arrange
    #     user_id = "user_id_1"
    #     from ib_adhoc_tasks.constants.enum import ViewType
    #     view_type = ViewType.LIST.value
    #     from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
    #     GroupByInfoFactory.reset_sequence(1)
    #     GroupByInfoFactory.create_batch(size=2, user_id=user_id)
    #     from ib_adhoc_tasks.tests.factories.storage_dtos import \
    #         GroupByResponseDTOFactory
    #     GroupByResponseDTOFactory.reset_sequence(1)
    #     group_by_response_dtos = [GroupByResponseDTOFactory()]
    #
    #     # Act
    #     actual_group_by_response_dtos = \
    #         storage.get_group_by_dtos(user_id=user_id, view_type=view_type)
    #
    #     # Assert
    #     assert actual_group_by_response_dtos == group_by_response_dtos

    # @pytest.mark.django_db
    # def test_add_group_by_adds_group_by_and_returns_group_by_response_dto(
    #         self, storage
    # ):
    #     # Arrange
    #     from ib_adhoc_tasks.tests.factories.storage_dtos import \
    #         AddOrEditGroupByParameterDTOFactory, GroupByResponseDTOFactory
    #     GroupByResponseDTOFactory.reset_sequence(1)
    #     group_by_response_dto = GroupByResponseDTOFactory()
    #     AddOrEditGroupByParameterDTOFactory.reset_sequence(1)
    #     add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
    #         group_by_id=None,
    #         group_by_key=group_by_response_dto.display_name,
    #         order=group_by_response_dto.order
    #     )
    #
    #     # Act
    #     actual_group_by_response_dto = storage.add_group_by(
    #         add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
    #     )
    #
    #     # Assert
    #     assert actual_group_by_response_dto == group_by_response_dto

    # @pytest.mark.django_db
    # def test_edit_group_by_adds_group_by_and_returns_group_by_response_dto(
    #         self, storage
    # ):
    #     # Arrange
    #     group_by_id = 1
    #     from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
    #     GroupByInfoFactory.reset_sequence(1)
    #     GroupByInfoFactory()
    #     from ib_adhoc_tasks.tests.factories.storage_dtos import \
    #         AddOrEditGroupByParameterDTOFactory
    #     AddOrEditGroupByParameterDTOFactory.reset_sequence(1)
    #     add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
    #         group_by_id=group_by_id, group_by_key="ASSIGNEE", order=2
    #     )
    #     from ib_adhoc_tasks.tests.factories.storage_dtos import \
    #         GroupByResponseDTOFactory
    #     GroupByResponseDTOFactory.reset_sequence(1)
    #     group_by_response_dto = GroupByResponseDTOFactory(
    #         group_by_key="ASSIGNEE", order=2
    #     )
    #
    #     # Act
    #     actual_group_by_response_dto = storage.edit_group_by(
    #         add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
    #     )
    #
    #     # Assert
    #     assert actual_group_by_response_dto == group_by_response_dto

    @pytest.mark.django_db
    def test_get_view_types_of_user_returns_view_types(self, storage):
        # Arrange
        user_id = "user_id_1"
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        GroupByInfoFactory.reset_sequence(1)
        GroupByInfoFactory.view_type.reset()
        GroupByInfoFactory.group_by.reset()
        GroupByInfoFactory.create_batch(size=3, user_id=user_id)
        from ib_adhoc_tasks.constants.enum import ViewType
        expected_view_types = [
            ViewType.LIST.value, ViewType.KANBAN.value, ViewType.LIST.value
        ]

        # Act
        view_types = storage.get_view_types_of_user(user_id=user_id)

        # Assert
        assert view_types == expected_view_types

    @pytest.mark.django_db
    def test_add_or_edit_group_by_for_list_view_and_returns_group_by_response_dto(
            self, storage
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            AddOrEditGroupByParameterDTOFactory, GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(1)
        group_by_response_dto = GroupByResponseDTOFactory()
        AddOrEditGroupByParameterDTOFactory.reset_sequence(1)
        add_or_edit_group_by_parameter_dto = AddOrEditGroupByParameterDTOFactory(
            group_by_key=group_by_response_dto.display_name,
            order=group_by_response_dto.order
        )

        # Act
        actual_group_by_response_dto = storage.add_or_edit_group_by_for_list_view(
            add_or_edit_group_by_parameter_dto=add_or_edit_group_by_parameter_dto
        )

        # Assert
        assert actual_group_by_response_dto == group_by_response_dto

    @pytest.mark.django_db
    def test_delete_all_user_group_by_deletes_all_records_of_user(
            self, storage
    ):
        # Arrange
        user_id = "user_id_1"
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        GroupByInfoFactory(user_id=user_id)

        # Act
        actual_group_by_response_dto = storage.delete_all_user_group_by(
            user_id=user_id
        )

        # Assert
        from ib_adhoc_tasks.models import GroupByInfo
        group_by_objects = GroupByInfo.objects.filter(user_id=user_id)
        assert len(group_by_objects) == 0

    @pytest.mark.django_db
    def test_add_group_by_for_kanban_view_in_bulk_and_returns_group_by_response_dtos(
            self, storage
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        from ib_adhoc_tasks.tests.factories.interactor_dtos import \
            GroupByParameterFactory, GroupBYKeyDTOFactory
        GroupByParameterFactory.reset_sequence(0)
        GroupByParameterFactory.view_type.reset()
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupBYKeyDTOFactory.group_by_key.reset()
        GroupBYKeyDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        GroupByResponseDTOFactory.order.reset()
        group_by_parameter = GroupByParameterFactory()
        group_by_key_dtos = [GroupBYKeyDTOFactory()]
        group_by_response_dtos = [GroupByResponseDTOFactory()]

        # Act
        actual_group_by_response_dtos = storage.add_group_by_for_kanban_view_in_bulk(
            group_by_parameter=group_by_parameter,
            group_by_key_dtos=group_by_key_dtos
        )

        # Assert
        assert actual_group_by_response_dtos == group_by_response_dtos
