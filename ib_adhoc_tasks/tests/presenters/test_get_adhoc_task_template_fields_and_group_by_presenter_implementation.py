import json

import pytest


class TestGetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_adhoc_tasks.presenters \
            .get_adhoc_task_template_fields_and_group_by_presenter_implementation \
            import GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation
        return GetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation()

    @pytest.fixture
    def group_by_fields_dtos(self):
        from ib_adhoc_tasks.tests.factories.storage_dtos import \
            GroupByResponseDTOFactory
        GroupByResponseDTOFactory.reset_sequence(0)
        GroupByResponseDTOFactory.order.reset()
        GroupByResponseDTOFactory.group_by_key.reset()
        GroupByResponseDTOFactory.display_name.reset()
        return GroupByResponseDTOFactory.create_batch(size=2)

    def test_given_valid_data_returns_success_response(
            self, presenter, snapshot, group_by_fields_dtos
    ):
        # Arrange
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldIdAndNameDTOFactory
        FieldIdAndNameDTOFactory.reset_sequence(0)
        field_dtos = FieldIdAndNameDTOFactory.create_batch(size=2)
        from ib_adhoc_tasks.interactors.dtos.dtos import \
            TemplateFieldsAndGroupByFieldsDTO
        template_fields_and_group_by_fields_dto = \
            TemplateFieldsAndGroupByFieldsDTO(
                group_by_fields_dtos=group_by_fields_dtos,
                field_dtos=field_dtos
            )

        # Act
        http_response = presenter.get_response_for_get_template_and_group_by_fields(
            template_fields_and_group_by_fields_dto=
            template_fields_and_group_by_fields_dto
        )

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response_dict")
