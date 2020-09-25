from ib_adhoc_tasks.constants.enum import ViewType, GroupByType

View_Types = [(item.value, item.value) for item in ViewType]
group_by_types = [(item.value, item.value) for item in GroupByType]
group_by_types_list = [item.value for item in GroupByType]
ADHOC_TEMPLATE_ID = "ADHOC"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
