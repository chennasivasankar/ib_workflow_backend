"""
Created on: 31/07/20
Author: Pavankumar Pamuru

"""
import json

import factory

from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, TaskTemplateWith2GoFsFactory, GoFFactory, \
    FieldFactory, StageModelFactory, StageActionFactory, \
    TaskTemplateInitialStageFactory, TaskTemplateGlobalConstantsFactory, \
    TaskFactory, TaskStatusVariableFactory, TaskGoFFactory, TaskGoFFieldFactory, \
    TaskStageModelFactory, GoFToTaskTemplateFactory


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
        fields = FieldFactory.create_batch(12, gof=factory.Iterator(gofs))
        GoFToTaskTemplateFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            gof=factory.Iterator(gofs)
        )
        stages = StageModelFactory.create_batch(
            6, task_template_id=factory.Iterator([
                'template_1', 'template_2', 'template_3'
            ]),
            field_display_config=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )
        actions = StageActionFactory.create_batch(12, stage=factory.Iterator(stages))
        TaskTemplateInitialStageFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            stage=factory.Iterator(stages)
        )
        # TaskTemplateGlobalConstantsFactory.create_batch(
        #     9, task_template_id=factory.Iterator([
        #         'template_1', 'template_2', 'template_3'
        #     ])
        # )

        tasks = TaskFactory.create_batch(
            6, template_id=factory.Iterator([
                'template_1', 'template_2', 'template_3',
            ])
        )
        TaskStatusVariableFactory.create_batch(
            18, task_id=factory.Iterator([
                '1', '2', '3', '4', '5', '6'
            ])
        )
        task_gofs = TaskGoFFactory.create_batch(
            6, task=factory.Iterator(tasks), gof_id=factory.Iterator(
                ['gof_1', 'gof_2', 'gof_3', 'gof_4', 'gof_5', 'gof_6']
            )

        )
        TaskGoFFieldFactory.create_batch(
            6, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        TaskStageModelFactory.create_batch(
            6, task=factory.Iterator(tasks),
            stage=factory.Iterator(stages)
        )
