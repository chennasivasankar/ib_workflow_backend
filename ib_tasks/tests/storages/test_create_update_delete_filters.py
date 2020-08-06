"""
Created on: 06/08/20
Author: Pavankumar Pamuru

"""
import factory
import pytest

from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    FilterFactory, \
    FieldFactory, FilterConditionFactory, FieldRoleFactory, \
    GoFToTaskTemplateFactory


@pytest.mark.django_db
class TestFilterStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.filter_storage_implementation import \
            FilterStorageImplementation
        return FilterStorageImplementation()

    @pytest.fixture
    def filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import CreateFilterDTOFactory
        CreateFilterDTOFactory.reset_sequence()
        return CreateFilterDTOFactory()

    @pytest.fixture
    def update_filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import UpdateFilterDTOFactory
        UpdateFilterDTOFactory.reset_sequence()
        return UpdateFilterDTOFactory()

    @pytest.fixture
    def condition_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import \
            CreateConditionDTOFactory
        CreateConditionDTOFactory.reset_sequence()
        return CreateConditionDTOFactory.create_batch(3)

    @pytest.fixture
    def new_filter_dto(self):
        from ib_tasks.tests.factories.filter_dtos import FilterDTOFactory
        FilterDTOFactory.reset_sequence()
        return FilterDTOFactory()

    @pytest.fixture
    def new_condition_dtos(self):
        from ib_tasks.tests.factories.filter_dtos import \
            ConditionDTOFactory
        ConditionDTOFactory.reset_sequence()
        return ConditionDTOFactory.create_batch(3)

    def test_validate_template_id_with_invalid_template_id(self, storage):
        # Arrange
        template_id = 'template_id'

        # Act
        from ib_tasks.exceptions.filter_exceptions import InvalidTemplateID
        with pytest.raises(InvalidTemplateID):
            storage.validate_template_id(
                template_id=template_id
            )

    def test_validate_template_id_with_valid_template_id(self, storage):
        # Arrange
        template_id = 'template_1'
        TaskTemplateFactory()

        # Act
        storage.validate_template_id(template_id=template_id)

    def test_validate_filter_id_with_invalid_filter_id(self, storage):
        # Arrange
        filter_id = 1

        # Act
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        with pytest.raises(InvalidFilterId):
            storage.validate_filter_id(filter_id=filter_id)

    def test_validate_filter_id_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        FilterFactory()

        # Act
        storage.validate_filter_id(filter_id=filter_id)

    def test_validate_user_with_filter_id_with_invalid_user_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '2'
        FilterFactory()

        # Act
        from ib_tasks.exceptions.filter_exceptions import UserNotHaveAccessToFilter
        with pytest.raises(UserNotHaveAccessToFilter):
            storage.validate_user_with_filter_id(
                filter_id=filter_id,
                user_id=user_id
            )

    def test_validate_user_with_filter_id_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '2'
        FilterFactory()

        # Act
        storage.validate_user_with_filter_id(
            filter_id=filter_id,
            user_id=user_id
        )

    def test_delete_filter_with_valid_filter_id(self, storage):
        # Arrange
        filter_id = 1
        user_id = '3'
        FilterFactory()

        # Act
        storage.delete_filter(
            filter_id=filter_id,
            user_id=user_id
        )

        # Assert
        from ib_tasks.models import Filter
        is_deleted = not Filter.objects.filter(id=filter_id).exists()

        assert is_deleted is True

    def test_create_filter_with_valid_details(
            self, storage, filter_dto, condition_dtos, snapshot):
        # Arrange
        template_id = 'template_0'
        TaskTemplateFactory(template_id=template_id)
        FieldFactory.create_batch(
            3, field_id=factory.Iterator(
                ['field_0', 'field_1', 'field_2']
            )
        )
        # Act
        filter_dto, condition_dtos = storage.create_filter(
            filter_dto=filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        snapshot.assert_match(filter_dto, 'filter_dto')
        snapshot.assert_match(condition_dtos, 'condition_dtos')

    def test_update_filter_with_valid_details(
            self, storage, update_filter_dto, condition_dtos, snapshot):
        # Arrange
        template_id = 'template_0'
        TaskTemplateFactory(template_id=template_id)
        FilterFactory(template_id=template_id)
        FilterConditionFactory.create_batch(3, filter_id=1)
        FieldFactory.create_batch(
            3, field_id=factory.Iterator(
                ['field_0', 'field_1', 'field_2']
            )
        )
        # Act
        filter_dto, condition_dtos = storage.update_filter(
            filter_dto=update_filter_dto,
            condition_dtos=condition_dtos
        )

        # Assert
        snapshot.assert_match(filter_dto, 'filter_dto')
        snapshot.assert_match(condition_dtos, 'condition_dtos')

    def test_validate_user_roles_with_field_ids_roles_return_error_message(
            self, storage):
        # Arrange
        fields = FieldRoleFactory.create_batch(3)
        field_ids = [field.field_id for field in fields]
        user_roles = ['User', 'Admin']

        # Act
        from ib_tasks.exceptions.filter_exceptions import \
            UserNotHaveAccessToFields
        with pytest.raises(UserNotHaveAccessToFields):
            storage.validate_user_roles_with_field_ids_roles(
                field_ids=field_ids, user_roles=user_roles
            )

    def test_validate_user_roles_with_field_ids_with_valid_roles(
            self, storage):
        # Arrange
        fields = FieldRoleFactory.create_batch(3)
        field_ids = [field.field_id for field in fields]
        user_roles = [field.role for field in fields]

        # Act
        storage.validate_user_roles_with_field_ids_roles(
            field_ids=field_ids, user_roles=user_roles
        )

    def test_get_field_ids_for_task_template_return_valid_field_ids(
            self, storage):
        # Arrange
        fields = FieldFactory.create_batch(3)
        gof_ids = [field.gof_id for field in fields]
        template_id = 'template_12'
        GoFToTaskTemplateFactory(gof_id=gof_ids[0])
        expected_field_ids = [field.field_id for field in fields]

        # Act
        actual_field_ids = storage.get_field_ids_for_task_template(
            field_ids=expected_field_ids[:2], template_id=template_id
        )

        # Assert
        assert actual_field_ids == expected_field_ids[:1]



