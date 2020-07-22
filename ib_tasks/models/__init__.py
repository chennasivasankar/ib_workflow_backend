from .action_permitted_roles import ActionPermittedRoles
from .stage import Stage
from .stage_actions import StageAction
from .task_status_variable import TaskStatusVariable
from .task_template import TaskTemplate
from .template_status_variables import TaskTemplateStatusVariables
from .task_template_global_constants import TaskTemplateGlobalConstants
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.gof import GoF
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.task_template_gof import TaskTemplateGoF
from ib_tasks.models.global_constant import GlobalConstant

__all__ = [
    "TaskTemplateGoF",
    "ActionPermittedRoles",
    "Stage",
    "StageAction",
    "TaskStatusVariable",
    "TaskTemplateStatusVariables",
    "TaskTemplateGlobalConstants",
    "Field", "FieldRole", "GoF", "GoFRole", "TaskTemplate", "GlobalConstant"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
