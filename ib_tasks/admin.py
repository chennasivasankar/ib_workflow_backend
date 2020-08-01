
from django.contrib import admin
from ib_tasks.models.gof import GoF
from ib_tasks.models.field import Field
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.task import Task
from ib_tasks.models.task_template_gofs import TaskTemplateGoFs
from ib_tasks.models.task_gof_field import TaskGoFField
from ib_tasks.models.task_gof import TaskGoF
from ib_tasks.models.task_log import TaskLog
from ib_tasks.models.task_stage import TaskStage

admin.site.register(GoF)
admin.site.register(Field)
admin.site.register(TaskTemplate)
admin.site.register(GoFRole)
admin.site.register(FieldRole)
admin.site.register(Task)
admin.site.register(TaskTemplateGoFs)
admin.site.register(TaskGoFField)
admin.site.register(TaskGoF)
admin.site.register(TaskLog)
admin.site.register(TaskStage)