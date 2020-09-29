import mock
import pytest

from ib_adhoc_tasks.adapters.task_service import TaskService


class TestGetAdhocTaskTemplateFieldsInteractor:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_adhoc_task_template_fields_presenter_implementation import \
            GetAdhocTaskTemplateFieldsPresenterImplementation
        return mock.create_autospec(
            GetAdhocTaskTemplateFieldsPresenterImplementation
        )

    @pytest.fixture
    def interactor(self):
        from ib_adhoc_tasks.interactors \
            .get_adhoc_task_template_fields_interactor import \
            AdhocTaskTemplateFieldsInteractor
        return AdhocTaskTemplateFieldsInteractor()

    @mock.patch.object(TaskService, "get_task_template_field_dtos")
    def test_given_valid_data_returns_fields_response(
            self, get_task_template_field_dtos_mock, interactor, presenter
    ):
        # Arrange
        project_id = "project_id_1"
        user_id = "user_id_1"
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=3)
        get_task_template_field_dtos_mock.return_value = field_dtos
        presenter.get_response_for_get_adhoc_task_template_fields \
            .return_value = mock.Mock()
        # todo need to look over this
        from ib_adhoc_tasks.constants.enum import GroupByKey
        for item in GroupByKey:
            from ib_adhoc_tasks.adapters.dtos import FieldIdAndNameDTO
            field_dtos.append(
                FieldIdAndNameDTO(
                    field_id=item.value, field_display_name=item.value
                )
            )

        # Act
        interactor.get_adhoc_task_template_fields_wrapper(
            project_id=project_id, user_id=user_id, presenter=presenter
        )

        # Assert
        from ib_adhoc_tasks.constants.constants import ADHOC_TEMPLATE_ID
        get_task_template_field_dtos_mock.assert_called_once_with(
            project_id=project_id, user_id=user_id,
            template_id=ADHOC_TEMPLATE_ID
        )
        presenter.get_response_for_get_adhoc_task_template_fields \
            .assert_called_once_with(field_dtos=field_dtos)





