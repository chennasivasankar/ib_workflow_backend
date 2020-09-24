import json

import pytest


class TestGetGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_adhoc_task_template_fields_presenter_implementation import \
            GetAdhocTaskTemplateFieldsPresenterImplementation
        return GetAdhocTaskTemplateFieldsPresenterImplementation()

    def test_get_response_for_get_adhoc_task_template_fields_returns_response_dict(
            self, presenter, snapshot
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        FieldIdAndNameDTOFactory.reset_sequence(0)
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=2)

        # Act
        http_response = presenter.get_response_for_get_adhoc_task_template_fields(
            field_dtos=field_dtos
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response_dict")
