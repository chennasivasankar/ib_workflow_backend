import factory

from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface import \
    ProjectTemplateFieldsDTO
from ib_tasks.interactors.presenter_interfaces.get_template_stage_flow_presenter_interface import \
    StageFlowCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    TaskWithCompleteStageDetailsDTO
from ib_tasks.tests.factories.interactor_dtos import \
    TaskStageAssigneeDetailsDTOFactory


class TaskIdWithStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdWithStageDetailsDTO

    task_id = factory.Sequence(lambda n: (n + 1))
    task_display_id = factory.sequence(
        lambda counter: "iBWF-{}".format(counter+1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    stage_display_name = factory.Sequence(
        lambda n: 'stage_display_%d' % (n + 1))
    stage_color = factory.Sequence(lambda n: "color_{}".format(n + 1))
    db_stage_id = factory.Sequence(lambda n: n + 1)


class TaskWithCompleteStageDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TaskWithCompleteStageDetailsDTO
    task_with_stage_details_dto = \
        factory.SubFactory(TaskIdWithStageDetailsDTOFactory)

    @factory.lazy_attribute
    def stage_assignee_dto(self):
        return [TaskStageAssigneeDetailsDTOFactory()]


class GetTaskStageCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskStageCompleteDetailsDTO

    task_id = factory.Sequence(lambda n: 'task_%d' % (n + 1))
    stage_color = factory.Sequence(lambda n: 'color_%d' % (n + 1))
    stage_id = factory.Sequence(lambda n: 'stage_%d' % (n + 1))
    display_name = "stage"
    db_stage_id = factory.Sequence(lambda n: (n+1))
    field_dtos = None
    action_dtos = None


class ProjectTemplateFieldsDTOFactory(factory.Factory):
    class Meta:
        model = ProjectTemplateFieldsDTO

    @factory.lazy_attribute
    def task_template_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import ProjectTemplateDTOFactory
        return [ProjectTemplateDTOFactory()]

    @factory.lazy_attribute
    def task_template_gofs_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import TaskTemplateGofsDTOFactory
        return [TaskTemplateGofsDTOFactory()]

    @factory.lazy_attribute
    def fields_dto(self):
        from ib_tasks.tests.factories.storage_dtos import FieldNameDTOFactory
        return [FieldNameDTOFactory()]


class StageFlowCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = StageFlowCompleteDetailsDTO

    @factory.lazy_attribute
    def stage_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import StageMinimalDTOFactory
        return [StageMinimalDTOFactory()]

    @factory.lazy_attribute
    def stage_flow_dtos(self):
        from ib_tasks.tests.factories.storage_dtos \
            import StageFlowDTOFactory
        return [StageFlowDTOFactory()]


class AllTasksOverviewDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AllTasksOverviewDetailsDTO

    @factory.lazy_attribute
    def task_with_complete_stage_details_dtos(self):
        TaskWithCompleteStageDetailsDTOFactory.reset_sequence()
        return [TaskWithCompleteStageDetailsDTOFactory()]

    @factory.lazy_attribute
    def task_fields_and_action_details_dtos(self):
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        return [GetTaskStageCompleteDetailsDTOFactory()]