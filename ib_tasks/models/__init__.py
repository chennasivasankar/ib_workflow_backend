
from .stage import Stage
from .stage_actions import StageAction
from .task_status_variable import TaskStatusVariable
from .task_template import TaskTemplate
from .template_status_variables import TaskTemplateStatusVariables

__all__ = [
    "Stage", "StageAction", "TaskTemplateStatusVariables",
    "TaskTemplate", "TaskStatusVariable"
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
