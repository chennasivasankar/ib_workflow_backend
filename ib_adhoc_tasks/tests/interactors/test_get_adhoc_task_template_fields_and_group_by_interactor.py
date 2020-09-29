import mock
import pytest

from ib_adhoc_tasks.tests.common_fixtures.interactors import \
    get_adhoc_template_fields_interactor_mock, get_group_by_interactor_mock


class TestGetAdhocTaskTemplateFieldsAndGroupBy:

    @pytest.fixture
    def storage(self):
        from ib_adhoc_tasks.interactors.storage_interfaces \
            .storage_interface import StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.interactors.presenter_interfaces \
            .get_adhoc_task_template_fields_and_group_by_presenter_interface import \
            GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface
        return mock.create_autospec(
            GetAdhocTaskTemplateFieldsAndGroupByPresenterInterface
        )

    @pytest.fixture
    def interactor(self, storage):
        from ib_adhoc_tasks.interactors \
            .get_adhoc_task_template_fields_and_group_by_interactor import \
            GetAdhocTaskTemplateFieldsAndGroupBy
        return GetAdhocTaskTemplateFieldsAndGroupBy(storage=storage)

    def test_given_valid_data_returns_group_by_and_template_fields(
            self, interactor, presenter, storage, mocker
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        group_by_fields_dtos = \
            GroupByResponseDTOFactory.create_batch(size=4)
        from ib_adhoc_tasks.constants.enum import ViewType
        project_id = "project_id_1"
        user_id = "user_id_1"
        view_type = ViewType.LIST.value
        get_group_by_interactor_mock(
            mocker=mocker, response=group_by_fields_dtos
        )
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        field_dtos = FieldIdAndNameDTOFactory()
        get_adhoc_template_fields_interactor_mock(
            mocker=mocker, response=field_dtos
        )
        from ib_adhoc_tasks.interactors.dtos.dtos import \
            TemplateFieldsAndGroupByFieldsDTO
        template_fields_and_group_by_fields_dto = \
            TemplateFieldsAndGroupByFieldsDTO(
                group_by_fields_dtos=group_by_fields_dtos,
                field_dtos=field_dtos
            )
        presenter.get_response_for_get_template_and_group_by_fields \
            .return_value = mock.Mock()

        # Act
        interactor.get_adhoc_task_template_fields_and_group_by_wrapper(
            project_id=project_id, user_id=user_id, view_type=view_type,
            presenter=presenter
        )

        # Assert
        presenter.get_response_for_get_template_and_group_by_fields \
            .assert_called_once_with(
            template_fields_and_group_by_fields_dto=
            template_fields_and_group_by_fields_dto
        )
