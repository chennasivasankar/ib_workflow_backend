from ib_adhoc_tasks.constants.enum import ViewType, GroupByKey

View_Types = [(item.value, item.value) for item in ViewType]
group_by_types = [(item.value, item.value) for item in GroupByKey]
group_by_types_list = [item.value for item in GroupByKey]
ADHOC_TEMPLATE_ID = "ADHOC"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
GROUP_BY_KEY_1 = GroupByKey.STAGE.value
GROUP_BY_KEY_2 = GroupByKey.ASSIGNEE.value
DISPLAY_DATE_FORMAT = "%b %d %Y"
