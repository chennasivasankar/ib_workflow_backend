
from django.contrib import admin

from ib_tasks.models import Stage, TaskStatusVariable
from ib_tasks.models.gof import GoF
from ib_tasks.models.field import Field
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.field_role import FieldRole

admin.site.register(GoF)
admin.site.register(Field)
admin.site.register(TaskTemplate)
admin.site.register(GoFRole)
admin.site.register(FieldRole)
admin.site.register(Stage)
admin.site.register(TaskStatusVariable)