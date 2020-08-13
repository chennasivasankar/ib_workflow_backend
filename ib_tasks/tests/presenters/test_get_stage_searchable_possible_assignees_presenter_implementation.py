import factory
import pytest


from ib_tasks.interactors.presenter_interfaces. \
    get_transition_template_presenter_interface import \
    CompleteTransitionTemplateDTO
from ib_tasks.tests.factories.storage_dtos import \
    TaskTemplateDTOFactory, UserFieldPermissionDTOFactory, FieldDTOFactory, \
    GoFToTaskTemplateDTOFactory, GoFDTOFactory, \
    FieldPermissionDTOFactory


class TestGetStageSearchablePossibleAssigneesPresenterImplementation:

    # @pytest.fixture(autouse=True)
    # def reset_sequence(self):
    #     TaskTemplateDTOFactory.reset_sequence()
    #     FieldDTOFactory.reset_sequence(1)
    #     GoFDTOFactory.reset_sequence(1)
    #     UserFieldPermissionDTOFactory.reset_sequence()
    #     GoFToTaskTemplateDTOFactory.reset_sequence()
    #     FieldPermissionDTOFactory.reset_sequence()
    #     FieldPermissionDTOFactory.is_field_writable.reset()
    #
    @pytest.fixture()
    def presenter(self):
        from ib_tasks.presenters.\
            get_stage_searchable_possible_assignees_presenter_implementation \
            import GetStageSearchablePossibleAssigneesPresenterImplementation

        presenter = \
            GetStageSearchablePossibleAssigneesPresenterImplementation()
        return presenter

    # def test_when_complete_transition_template_details_exists(
    #         self, snapshot, presenter):
    #     # Arrange
    #     expected_gof_ids = ['gof_1', 'gof_2']
    #     expected_field_ids = ["field_1", "field_2", "field_3", "field_4"]
    #
    #     transition_template_dto = TaskTemplateDTOFactory.create()
    #     gof_dtos = GoFDTOFactory.create_batch(size=2)
    #     field_dtos = FieldDTOFactory.create_batch(
    #         size=4, field_id=factory.Iterator(expected_field_ids),
    #         gof_id=factory.Iterator(expected_gof_ids)
    #     )
    #     UserFieldPermissionDTOFactory.create_batch(size=4)
    #     gofs_of_template_dtos = \
    #         GoFToTaskTemplateDTOFactory.create_batch(size=2)
    #     field_with_permissions_dtos = \
    #         FieldPermissionDTOFactory.create_batch(
    #             size=2, field_dto=factory.Iterator(field_dtos),
    #             is_field_writable=factory.Iterator([False, True])
    #         )
    #
    #     complete_transition_template_dto = CompleteTransitionTemplateDTO(
    #         transition_template_dto=transition_template_dto,
    #         gof_dtos=gof_dtos,
    #         gofs_of_transition_template_dtos=gofs_of_template_dtos,
    #         field_with_permissions_dtos=field_with_permissions_dtos
    #     )
    #
    #     # Act
    #     presenter_response_object = presenter.get_transition_template_response(
    #         complete_transition_template_dto=complete_transition_template_dto
    #     )
    #
    #     # Assert
    #     import json
    #     response_content = json.loads(presenter_response_object.content)
    #
    #     snapshot.assert_match(response_content, 'transition_template')

    def test_raise_invalid_offset_exception(self, snapshot, presenter):
        # Act
        response_object = presenter.raise_invalid_offset_exception()

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_limit_exception(self, snapshot, presenter):
        # Act
        response_object = presenter.raise_invalid_limit_exception()

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_stage_id_exception(self, snapshot, presenter):
        # Arrange
        stage_id = 100
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
        err = InvalidStageId(stage_id)

        # Act
        response_object = presenter.raise_invalid_stage_id_exception(err)

        # Assert
        import json
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')
