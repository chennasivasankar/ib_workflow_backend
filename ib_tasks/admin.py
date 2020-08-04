from django.contrib import admin

from ib_tasks.models import Stage, TaskTemplateStatusVariable, StageAction, \
    TaskTemplateInitialStage, TaskStatusVariable
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.gof import GoF
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.task import Task
from ib_tasks.models.task_gof import TaskGoF
from ib_tasks.models.task_gof_field import TaskGoFField
from ib_tasks.models.task_log import TaskLog
from ib_tasks.models.task_stage import TaskStage
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.task_template_gofs import TaskTemplateGoFs


admin.site.register(GoF)
admin.site.register(Field)
admin.site.register(TaskTemplate)
admin.site.register(GoFRole)
admin.site.register(FieldRole)
admin.site.register(Stage)
admin.site.register(TaskTemplateStatusVariable)
admin.site.register(StageAction)
admin.site.register(TaskTemplateInitialStage)
admin.site.register(TaskStatusVariable)
admin.site.register(TaskStage)
admin.site.register(TaskGoF)


class TaskGofFieldAdmin(admin.ModelAdmin):
    list_display = ('field_id', "field_response", 'task_gof_id')


admin.site.register(TaskGoFField, TaskGofFieldAdmin)
admin.site.register(TaskTemplateGoFs)


class TaskStageInline(admin.StackedInline):
    model = TaskStage
    extra = 3


class TaskGoFInline(admin.StackedInline):
    model = TaskGoF


class TaskTemplateInline(admin.StackedInline):
    model = TaskTemplate


class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskStageInline, TaskGoFInline, ]
    list_display = ('id',)


admin.site.register(Task, TaskAdmin)

admin.site.register(TaskLog)
