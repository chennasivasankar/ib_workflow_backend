import pytest

from ib_tasks.constants.enum import ViewType
from ib_tasks.storages.fields_storage_implementation import \
    FieldsStorageImplementation
from ib_tasks.tests.factories.models import (
    StageModelFactory, TaskFactory, TaskTemplateFactory,
    CurrentTaskStageModelFactory)
from ib_tasks.tests.factories.storage_dtos import TemplateStagesDTOFactory


@pytest.mark.django_db
class TestGetFieldIds:

    @pytest.fixture()
    def get_task_template_stage_dtos(self):
        TemplateStagesDTOFactory.reset_sequence()
        return TemplateStagesDTOFactory.create_batch(size=3)

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        StageModelFactory()
        import json
        StageModelFactory(card_info_kanban=json.dumps(
            ['field_id_3', 'field_id_4']),
            card_info_list=json.dumps(
                ['field_id_5', 'field_id_6'])
        )
        StageModelFactory(card_info_kanban=json.dumps(
            ['field_id_5', 'field_id_6']),
            card_info_list=json.dumps(
                ['field_id_7', 'field_id_8'])
        )
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.create_batch(size=3)
        CurrentTaskStageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.create_batch(size=4)

    @pytest.fixture()
    def get_task_template_stage_dtos_with_one_task_with_two_stages(self):
        TemplateStagesDTOFactory.reset_sequence()
        templates = TemplateStagesDTOFactory.create_batch(
            size=2, task_id=1, task_template_id="task_template_id_0")
        templates.append(TemplateStagesDTOFactory(task_id=2))
        templates.append(TemplateStagesDTOFactory(task_id=2))
        return templates

    @pytest.fixture()
    def populate_data_for_one_task_in_two_stages(self):
        StageModelFactory.reset_sequence()
        StageModelFactory(task_template_id="task_template_id_0")
        import json
        StageModelFactory(card_info_kanban=json.dumps(
            ['field_id_3', 'field_id_4']),
            card_info_list=json.dumps(
                ['field_id_5', 'field_id_6']),
            task_template_id="task_template_id_0")
        StageModelFactory(card_info_kanban=json.dumps(
            ['field_id_5', 'field_id_6']),
            card_info_list=json.dumps(
                ['field_id_7', 'field_id_8'])
        )
        StageModelFactory(card_info_kanban=json.dumps(
            ['field_id_7', 'field_id_8']),
            card_info_list=json.dumps(
                ['field_id_9', 'field_id_10'])
        )
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(size=3)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.create_batch(size=3)
        CurrentTaskStageModelFactory.create_batch(size=4)

    @pytest.fixture()
    def get_task_template_stage_dtos_with_two_tasks_on_stage(self):
        TemplateStagesDTOFactory.reset_sequence()
        templates = TemplateStagesDTOFactory.create_batch(
            size=2, stage_id="stage_id_0",
            task_template_id="task_template_id_0")
        return templates

    def test_get_field_ids_when_view_type_is_list(
            self, get_task_template_stage_dtos, populate_data, snapshot):
        # Arrange
        view_type = ViewType.LIST.value
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_field_ids(get_task_template_stage_dtos,
                                         view_type)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_field_ids_when_view_type_is_kanban(
            self, get_task_template_stage_dtos, populate_data, snapshot):
        # Arrange
        view_type = ViewType.KANBAN.value
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_field_ids(get_task_template_stage_dtos,
                                         view_type)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_field_ids_when_one_task_is_in_two_stages(
            self,
            get_task_template_stage_dtos_with_one_task_with_two_stages,
            populate_data_for_one_task_in_two_stages,
            snapshot):
        # Arrange
        view_type = ViewType.LIST.value
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_field_ids(
            get_task_template_stage_dtos_with_one_task_with_two_stages,
            view_type)

        # Assert
        snapshot.assert_match(response, "response")

    def test_get_field_ids_when_two_tasks_are_in_one_stage(
            self, get_task_template_stage_dtos_with_two_tasks_on_stage,
            populate_data,
            snapshot):
        # Arrange
        view_type = ViewType.LIST.value
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_field_ids(
            get_task_template_stage_dtos_with_two_tasks_on_stage, view_type)

        # Assert
        snapshot.assert_match(response, "response")
