"""
Created on: 31/07/20
Author: Pavankumar Pamuru

"""
import json

import factory

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.models import Field
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, GoFFactory, \
    StageModelFactory, StageActionFactory, \
    TaskTemplateInitialStageFactory, TaskFactory, TaskStatusVariableFactory, \
    TaskGoFFactory, TaskGoFFieldFactory, \
    CurrentTaskStageModelFactory, GoFToTaskTemplateFactory


class FieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Field

    gof = factory.SubFactory(GoFFactory)
    field_id = factory.Sequence(lambda counter: "FIELD_ID-{}".format(counter))
    display_name = factory.Sequence(
        lambda counter: "DISPLAY_NAME-{}".format(counter)
    )
    field_type = FieldTypes.PLAIN_TEXT.value
    field_values = '["mr", "mrs"]'
    help_text = factory.Sequence(lambda counter: "HELP_TEXT_{}".format(counter))
    required = True


class DataCreation:

    @staticmethod
    def create_task_templates():
        tts = TaskTemplateFactory.create_batch(3)
        TaskTemplateStatusVariableFactory.create_batch(
            16, task_template_id=factory.Iterator([
                'template_1', 'template_2', 'template_3'
            ])
        )
        gofs = GoFFactory.create_batch(6)
        fields = FieldFactory.create_batch(24, gof=factory.Iterator(gofs))
        GoFToTaskTemplateFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            gof=factory.Iterator(gofs)
        )
        stages = StageModelFactory.create_batch(
            6, task_template_id=factory.Iterator([
                'template_1', 'template_2', 'template_3'
            ]),
            card_info_kanban=json.dumps([
                "FIELD_ID-0", "FIELD_ID-1", "FIELD_ID-2", "FIELD_ID-3",
                "FIELD_ID-4", "FIELD_ID-5", "FIELD_ID-6", "FIELD_ID-7",
                "FIELD_ID-8", "FIELD_ID-9", "FIELD_ID-10", "FIELD_ID-11",
                "FIELD_ID-12", "FIELD_ID-13", "FIELD_ID-14", "FIELD_ID-15",
                "FIELD_ID-16", "FIELD_ID-17", "FIELD_ID-18", "FIELD_ID-19",
                "FIELD_ID-20", "FIELD_ID-21", "FIELD_ID-22", "FIELD_ID-23"
            ]),
            card_info_list=json.dumps([
                "FIELD_ID-0", "FIELD_ID-1", "FIELD_ID-2", "FIELD_ID-3",
                "FIELD_ID-4", "FIELD_ID-5", "FIELD_ID-6", "FIELD_ID-7",
                "FIELD_ID-8", "FIELD_ID-9", "FIELD_ID-10", "FIELD_ID-11",
                "FIELD_ID-12", "FIELD_ID-13", "FIELD_ID-14", "FIELD_ID-15",
                "FIELD_ID-16", "FIELD_ID-17", "FIELD_ID-18", "FIELD_ID-19",
                "FIELD_ID-20", "FIELD_ID-21", "FIELD_ID-22", "FIELD_ID-23"
            ])
        )
        actions = StageActionFactory.create_batch(24, stage=factory.Iterator(stages))
        TaskTemplateInitialStageFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            stage=factory.Iterator(stages)
        )

        tasks = TaskFactory.create_batch(
            20, template_id=factory.Iterator([
                'template_1', 'template_2', 'template_3',
            ])
        )
        TaskStatusVariableFactory.create_batch(
            60, task_id=factory.Iterator([
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'
            ])
        )
        task_gofs = TaskGoFFactory.create_batch(
            20, task=factory.Iterator(tasks), gof_id=factory.Iterator(
                ['gof_1', 'gof_2', 'gof_3', 'gof_4', 'gof_5', 'gof_6']
            )

        )
        TaskGoFFieldFactory.create_batch(
            20, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        CurrentTaskStageModelFactory.create_batch(
            20, task=factory.Iterator(tasks),
            stage=factory.Iterator(stages)
        )
